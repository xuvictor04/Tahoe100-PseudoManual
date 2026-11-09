---
symbol: "RNF40"
type: "gene"
col: 2383
ensembl_id: "ENSG00000103549"
name: "ring finger protein 40"
location: "16p11.2"
module: 127
arm: "+"
pooled_cpm: 44.27
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 5
n_dd_up_clean: 18
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# RNF40

*ring finger protein 40* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.03× (z +19.6, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.670× (z -7.6, q 2e-11, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF548]] (+0.72, fdr 7e-06), [[PRPF31]] (+0.69, fdr 7e-06), [[KAT5]] (+0.68, fdr 7e-06); moves opposite to [[TBC1D4]] (-0.57, fdr 2e-05), [[HPRT1]] (-0.56, fdr 2e-05), [[NAP1L1]] (-0.56, fdr 1e-05).
> It is in [[Module 127]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2383.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.03×** | +19.6 | 0e+00 | 45/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.21×** | +14.7 | 0e+00 | 47/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.24×** | +12.0 | 5e-31 | 39/48 (SW480, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.83×** | +11.8 | 4e-30 | 46/48 (SW480, RKO, …) | two highest doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.75×** | +10.9 | 8e-26 | 41/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +9.6 | 7e-20 | 37/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +9.6 | 7e-20 | 41/48 (SW480, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +9.0 | 1e-17 | 38/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +7.6 | 3e-12 | 35/48 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +7.0 | 1e-10 | 29/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +6.8 | 5e-10 | 31/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +6.4 | 8e-09 | 33/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.33×** | +5.5 | 2e-06 | 29/48 (SW480, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +5.1 | 1e-05 | 26/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.9 | 3e-05 | 26/48 (LoVo, HS-578T, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.4 | 3e-04 | 24/48 (PANC-1, SW48, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.4 | 4e-04 | 25/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2383.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.670×** | -7.6 | 2e-11 | 34/48 (H4, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.802×** | -6.1 | 2e-07 | 28/48 (SNU-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.737×** | -6.0 | 4e-07 | 32/48 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.750×** | -5.4 | 8e-06 | 28/48 (HEC-1-A, C32, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.806×** | -4.2 | 0.002 | 21/48 (A498, J82, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.878× | -3.6 | 0.027 | 12/48 (SHP-77, SW 900, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.954× | -3.2 | 0.10 | 0/49 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2383. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 41.2 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.36× (z +14.5) | — |
| [[SW480 (line)]] | alt | 37.5 | 6 | 0 | [[TAK-901 (drug)]] 5 µM 7.15× (z +12.7) | — |
| [[HEC-1-A (line)]] | alt | 52.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 43.3 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +10.2) | — |
| [[RKO (line)]] | wt | 37.7 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 12.8× (z +11.2) | — |
| [[KATO III (line)]] | alt | 56.9 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.19× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 44.1 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.19× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 43.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -11.2) |
| [[A498 (line)]] | wt | 62.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -9.8) |
| [[HT-29 (line)]] | alt | 42.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.1) | — |
| [[LoVo (line)]] | wt | 39.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.7) | — |
| [[LOX-IMVI (line)]] | wt | 35.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +16.9) | — |
| [[NCI-H1573 (line)]] | alt | 55.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +18.5) | — |
| [[A-172 (line)]] | wt | 51.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.2) | — |
| [[A-427 (line)]] | wt | 48.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.39× (z +9.2) | — |
| [[A549 (line)]] | wt | 46.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.5) | — |
| [[AsPC-1 (line)]] | alt | 44.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -10.5) |
| [[COLO 205 (line)]] | alt | 46.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 13.7× (z +9.8) | — |
| [[H4 (line)]] | wt | 47.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 67.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 26.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +14.1) | — |
| [[NCI-H1792 (line)]] | alt | 36.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 45.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 40.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 37.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +13.2) | — |
| [[RPMI-7951 (line)]] | alt | 53.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 39.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 37.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 39.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0918× (z -9.7) ⚠ toxic |
| [[SW1417 (line)]] | alt | 58.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2383), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF548]] | +0.72 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[PRPF31]] | +0.69 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[KAT5]] | +0.68 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[SRP68]] | +0.67 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[PRPF6]] | +0.67 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[ABCF3]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[GPKOW]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[EXOC3]] | +0.64 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[SART1]] | +0.64 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[DHX16]] | +0.64 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[EDC3]] | +0.62 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[USP19]] | +0.61 | +0.56 / +0.64 | both halves | 1e-05 | STRING 405 |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D4]] | -0.57 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[HPRT1]] | -0.56 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[NAP1L1]] | -0.56 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[METTL21A]] | -0.55 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[HINT1]] | -0.54 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[B3GALNT2]] | -0.53 | -0.56 / -0.36 | both halves | 1e-04 |  |
| [[PALS2]] | -0.52 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[DGKE]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[ARHGAP21]] | -0.50 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[MEMO1]] | -0.50 | -0.58 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RNF40's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.685). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.1, -2.6); signed map (-13.0, -28.2). **Vector** length 90.0, 21.1% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.1 | +14.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.7 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.7 | +0.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | +5.5 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.4 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +12.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +5.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +4.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -7.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -6.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.7 | +0.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.2 | -0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -0.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[vincristine (drug)]] 0.05 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 40 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,761,745-30,776,307 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0661, RBP95, BRE1B, STARING |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 2 pathways, smallest: E3 ubiquitin ligases ubiquitinate target proteins; Protein ubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [O75150](https://www.uniprot.org/uniprotkb/O75150) (E3 ubiquitin-protein ligase BRE1B):

> Component of the RNF20/40 E3 ubiquitin-protein ligase complex that mediates monoubiquitination of 'Lys-120' of histone H2B (H2BK120ub1). H2BK120ub1 gives a specific tag for epigenetic transcriptional activation and is also prerequisite for histone H3 'Lys-4' and 'Lys-79' methylation (H3K4me and H3K79me, respectively). It thereby plays a central role in histone code and gene regulation. The RNF20/40 complex forms a H2B ubiquitin ligase complex in cooperation with the E2 enzyme UBE2A or UBE2B; …

**Summary**, from NCBI Gene [9810](https://www.ncbi.nlm.nih.gov/gene/9810):

> The protein encoded by this gene contains a RING finger, a motif known to be involved in protein-protein and protein-DNA interactions. This protein was reported to interact with the tumor suppressor protein RB1. Studies of the rat counterpart suggested that this protein may function as an E3 ubiquitin-protein ligase, and facilitate the ubiquitination and degradation of syntaxin 1, which is an essential component of the neurotransmitter release machinery. Multiple alternatively spliced …

**Accessions** — [HGNC:16867](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16867) · Entrez [9810](https://www.ncbi.nlm.nih.gov/gene/9810) · UniProt [O75150](https://www.uniprot.org/uniprotkb/O75150) · Ensembl [ENSG00000103549](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103549)

## Data

Gene col 2383: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2383); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2383, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2383]; `tensor/DDL_lfc|DDL_z.npy` [2383]; `embed/gene_vectors.npy` [2383]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2383 or target_col == 2383). Every well: [[RNF40 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF40.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
