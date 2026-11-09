---
symbol: "BOLA1"
type: "gene"
col: 10896
ensembl_id: "ENSG00000178096"
name: "bolA family member 1"
location: "1q21.2"
module: 80
arm: "+"
pooled_cpm: 5.85
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# BOLA1

*bolA family member 1* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.18× (z +29.9, q 0e+00, up in 37 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.675× (z -4.0, q 0.035, down in 13 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.132×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (PANC-1 0.223×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C11orf71]] (+0.77, fdr 7e-06), [[NEK8]] (+0.77, fdr 7e-06), [[MZF1-AS1]] (+0.72, fdr 7e-06); moves opposite to [[ACTR5]] (-0.68, fdr 9e-06), [[NUDT21]] (-0.68, fdr 1e-05), [[NDRG3]] (-0.66, fdr 1e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10896.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.18×** | +29.9 | 0e+00 | 37/37 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **6.29×** | +26.1 | 0e+00 | 34/37 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.50×** | +12.1 | 2e-31 | 31/37 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.20×** | +11.2 | 5e-27 | 29/40 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.86×** | +10.1 | 4e-22 | 28/38 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.25×** | +8.1 | 4e-14 | 28/45 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.13×** | +7.6 | 3e-12 | 23/42 (A-172, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.13×** | +7.6 | 3e-12 | 20/37 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +5.9 | 2e-07 | 3/8 (NCI-H2030, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.3 | 7e-06 | 16/46 (A-172, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.67×** | +5.1 | 2e-05 | 18/44 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.55×** | +4.4 | 6e-04 | 13/45 (SW480, NCI-H23, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +4.3 | 7e-04 | 10/44 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +3.9 | 0.003 | 14/43 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.66×** | +3.6 | 0.011 | 4/39 (HEC-1-A, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.41×** | +3.1 | 0.052 | 6/35 (C32, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10896.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.132×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (PANC-1 0.223×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.675×** | -4.0 | 0.035 | 13/43 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Gallic acid (drug)]] 5 µM |  | 0.788× | -3.5 | 0.16 | 6/45 (hTERT-HPNE, NCI-H23, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.729× | -3.1 | 0.37 | 11/35 (NCI-H460, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10896. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.08 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.47× (z +15.0) | — |
| [[C32 (line)]] | wt | 7.95 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 59.0× (z +19.5) | — |
| [[PANC-1 (line)]] | alt | 8.34 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.78× (z +16.1) | [[Digitoxin (drug)]] 5 µM 0.132× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.223× (z -9.0) |
| [[A498 (line)]] | wt | 3.78 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +12.5) | — |
| [[COLO 205 (line)]] | alt | 5.78 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 6.03 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.31× (z +13.4) | — |
| [[HOP62 (line)]] | alt | 3.54 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +13.9) | — |
| [[hTERT-HPNE (line)]] | wt | 3.40 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.6× (z +11.2) | — |
| [[J82 (line)]] | alt | 5.55 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.38× (z +9.6) | — |
| [[KATO III (line)]] | alt | 5.98 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.94× (z +11.9) | — |
| [[LoVo (line)]] | wt | 4.55 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +16.1) | — |
| [[LOX-IMVI (line)]] | wt | 4.41 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.6× (z +14.8) | — |
| [[LS 180 (line)]] | wt | 3.94 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.22× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 16.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +10.8) | — |
| [[NCI-H2030 (line)]] | alt | 9.55 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +11.6) | — |
| [[NCI-H23 (line)]] | alt | 25.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +14.2) | — |
| [[NCI-H2347 (line)]] | alt | 3.89 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +13.2) | — |
| [[NCI-H460 (line)]] | wt | 4.72 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +17.8) | — |
| [[SK-MEL-2 (line)]] | alt | 9.72 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.13× (z +11.2) | — |
| [[A-172 (line)]] | wt | 7.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.89× (z +12.4) | — |
| [[AsPC-1 (line)]] | alt | 3.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.2× (z +11.4) | — |
| [[BT-474 (line)]] | alt | 2.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.9× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 6.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.32× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 4.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 4.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.51× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 28.0× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 6.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.35× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 7.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.57× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 5.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.50× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 3.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.0× (z +11.6) | — |
| [[A-427 (line)]] | wt | 7.51 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10896), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf71]] | +0.77 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[NEK8]] | +0.77 | +0.82 / +0.60 | both halves | 7e-06 |  |
| [[MZF1-AS1]] | +0.72 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[AP5S1]] | +0.71 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.71 | +0.78 / +0.49 | both halves | 1e-05 |  |
| [[ZNF341-AS1]] | +0.71 | +0.72 / +0.48 | both halves | 2e-05 |  |
| [[MAP3K20-AS1]] | +0.70 | +0.76 / +0.51 | both halves | 1e-05 |  |
| [[EIF4EBP3]] | +0.70 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[GPR137]] | +0.70 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[ARMC5]] | +0.70 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[RBBP6]] | +0.70 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[PPP1R12A-AS2]] | +0.70 | +0.79 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTR5]] | -0.68 | -0.64 / -0.57 | both halves | 9e-06 |  |
| [[NUDT21]] | -0.68 | -0.68 / -0.56 | both halves | 1e-05 |  |
| [[NDRG3]] | -0.66 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[FAR1]] | -0.65 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[AP3M2]] | -0.64 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[PLA2G12A]] | -0.63 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[EEF1E1]] | -0.63 | -0.57 / -0.67 | both halves | 9e-06 |  |
| [[GGCT]] | -0.63 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[PARP1]] | -0.63 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[SKP2]] | -0.63 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[SLC23A2]] | -0.63 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[METAP1]] | -0.62 | -0.71 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BOLA1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MIR583HG]] | B | MIR583HG activity raises BOLA1's level | lines that do not express MIR583HG (10) vs lines expressing it (40) | 1.48× lower at baseline in the lines without MIR583HG | 0.095 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RGS17, GNAI1, KLF12; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.758). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.1, 10.4); signed map (21.4, -6.3). **Vector** length 75.5, 14.0% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.6 | +26.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +29.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +11.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +7.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +12.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +7.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +2.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.5 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +3.1 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.0 | +1.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -2.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.4 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -2.3 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | bolA family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:149,887,890-149,900,798 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-143 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3E2](https://www.uniprot.org/uniprotkb/Q9Y3E2) (BolA-like protein 1):

> Acts as a mitochondrial iron-sulfur (Fe-S) cluster assembly factor that facilitates (Fe-S) cluster insertion into a subset of mitochondrial proteins (By similarity). Probably acts together with the monothiol glutaredoxin GLRX5. May protect cells against oxidative stress.

**Summary**, from NCBI Gene [51027](https://www.ncbi.nlm.nih.gov/gene/51027):

> Predicted to be involved in cell redox homeostasis; intracellular iron ion homeostasis; and iron-sulfur cluster assembly. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24263](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24263) · Entrez [51027](https://www.ncbi.nlm.nih.gov/gene/51027) · UniProt [Q9Y3E2](https://www.uniprot.org/uniprotkb/Q9Y3E2) · Ensembl [ENSG00000178096](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178096)

## Data

Gene col 10896: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10896); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10896, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10896]; `tensor/DDL_lfc|DDL_z.npy` [10896]; `embed/gene_vectors.npy` [10896]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10896 or target_col == 10896). Every well: [[BOLA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BOLA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
