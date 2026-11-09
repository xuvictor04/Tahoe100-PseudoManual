---
symbol: "NANOS3"
type: "gene"
col: 11923
ensembl_id: "ENSG00000187556"
name: "nanos C2HC-type zinc finger 3"
location: "19p13.12"
module: 80
arm: "+"
pooled_cpm: 2.53
n_lines_expressing: 48
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# NANOS3

*nanos C2HC-type zinc finger 3* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 9.08× (z +25.5, q 0e+00, up in 28 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.515× (z -5.4, q 3e-05, down in 21 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMRN2]] (+0.77, fdr 7e-06), [[NEPRO-AS1]] (+0.75, fdr 1e-05), [[IL34]] (+0.74, fdr 7e-06); moves opposite to [[SLC9A6]] (-0.67, fdr 5e-05), [[RPA1]] (-0.66, fdr 4e-05), [[VDAC3]] (-0.65, fdr 2e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC00460]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11923.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **9.08×** | +25.5 | 0e+00 | 28/30 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.55×** | +12.4 | 1e-32 | 20/31 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **3.85×** | +10.6 | 7e-24 | 30/37 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +8.4 | 9e-15 | 1/4 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.63×** | +7.3 | 3e-11 | 1/6 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.08×** | +6.0 | 2e-07 | 3/12 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.02×** | +5.7 | 8e-07 | 14/35 (HEC-1-A, HS-578T, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.6 | 2e-06 | 12/32 (NCI-H460, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +4.4 | 6e-04 | 13/36 (BT-474, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.4 | 6e-04 | 10/40 (PANC-1, NCI-H460, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +4.2 | 0.001 | 12/40 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +3.8 | 0.006 | 9/40 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +3.3 | 0.047 | 6/41 (RKO, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +3.2 | 0.062 | 7/38 (NCI-H460, A-427, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11923.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.515×** | -5.4 | 3e-05 | 21/40 (SW480, SW1417, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.551×** | -4.9 | 3e-04 | 18/41 (A-427, SW48, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.563×** | -4.7 | 5e-04 | 19/40 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~18% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11923. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 3.61 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0360× (z -9.3) |
| [[PANC-1 (line)]] | alt | 2.58 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.45× (z +12.0) | [[Digitoxin (drug)]] 5 µM 0.0699× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +11.9) | — |
| [[CFPAC-1 (line)]] | alt | 1.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.1× (z +10.1) | — |
| [[HepG2_C3A (line)]] | wt | 5.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 2.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 3.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +10.5) | — |
| [[J82 (line)]] | alt | 5.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 2.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.7× (z +12.5) | — |
| [[NCI-H2030 (line)]] | alt | 0.977 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 1.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 6.91 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 4.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 4.38 | 0 | 1 | — | [[Budesonide (drug)]] 0.5 µM 0.0826× (z -8.7) |
| [[SW48 (line)]] | wt | 5.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +9.8) | — |
| [[SW480 (line)]] | alt | 4.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +8.8) | — |
| [[A498 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.781 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.558 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.594 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.723 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.879 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.727 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.672 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.727 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11923), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMRN2]] | +0.77 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[NEPRO-AS1]] | +0.75 | +0.78 / +0.54 | both halves | 1e-05 |  |
| [[IL34]] | +0.74 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[ANGPT2]] | +0.72 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[MMP25]] | +0.72 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[ENO3]] | +0.71 | +0.77 / +0.43 | both halves | 3e-05 |  |
| [[GRIK5]] | +0.70 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[SSUH2]] | +0.70 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ZNF620]] | +0.70 | +0.74 / +0.49 | both halves | 1e-05 |  |
| [[ZC3H4]] | +0.70 | +0.70 / +0.42 | both halves | 4e-05 |  |
| [[ZFHX2]] | +0.69 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[HIVEP2-DT]] | +0.69 | +0.72 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A6]] | -0.67 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[RPA1]] | -0.66 | -0.74 / -0.42 | both halves | 4e-05 | pathway: Reproduction |
| [[VDAC3]] | -0.65 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[GLG1]] | -0.64 | -0.69 / -0.47 | both halves | 2e-05 |  |
| [[ECI2]] | -0.63 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[SAP130]] | -0.63 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[GMCL1]] | -0.62 | -0.62 / -0.38 | both halves | 6e-05 |  |
| [[STRN]] | -0.62 | -0.63 / -0.30 | both halves | 2e-04 |  |
| [[MMS19]] | -0.62 | -0.62 / -0.46 | both halves | 2e-05 |  |
| [[WDR5]] | -0.61 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[GIT2]] | -0.61 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[KATNB1]] | -0.61 | -0.58 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00460]] | B | LINC00460 activity raises NANOS3's level | lines that do not express LINC00460 (31) vs lines expressing it (19) | 1.37× lower at baseline in the lines without LINC00460 | 0.015 | ⚠ within organs, on part of the lines; also absent: LINC02335, LINC01605, KISS1 |
| [[HDAC6]] | B | HDAC6 activity raises NANOS3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SLCO5A1]] | B | SLCO5A1 activity lowers NANOS3's level | lines that do not express SLCO5A1 (6) vs lines expressing it (44) | 1.75× higher at baseline in the lines without SLCO5A1 | 0.057 | ⚠ within organs, on part of the lines; also absent: EFCAB3P1; maybe low, not absent |
| [[OXTR]] | B | OXTR activity strengthens NANOS3's drug response | lines that do not express OXTR (5) vs lines expressing it (36) | the lines without OXTR respond 0.72× as strongly (z diff +0.79); strongest at Idarubicin (hydrochloride) 5 µM: 0.33x vs 1.76x (z diff +6.3) | 0.081 | ⚠ within organs, on part of the lines; also absent: IPCEF1, SSUH2, OPN3; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[DLX2]] | B | DLX2 activity raises NANOS3's level | lines that do not express DLX2 (8) vs lines expressing it (42) | 1.27× lower at baseline in the lines without DLX2 | 0.092 | ⚠ within organs, on part of the lines; also absent: LINC01145-1, SCHIP1, NPHS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.798). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.0, 10.2); signed map (25.0, 6.2). **Vector** length 66.1, 10.4% of its response variance represented; |z| ≥ 3 in 1,121 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.9 | +25.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.3 | +10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +4.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +3.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.3 | -4.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.1 | -5.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.7 | -4.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.4 | -0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | nanos C2HC-type zinc finger 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:13,862,063-13,880,757 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NANOS1L, NOS3 |
| Gene groups (HGNC) | Zinc fingers Nanos C2HC-type |
| Reactome | 2 pathways, smallest: Specification of primordial germ cells; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [P60323](https://www.uniprot.org/uniprotkb/P60323) (Nanos homolog 3):

> Plays a role in the maintenance of the undifferentiated state of germ cells regulating the spermatogonia cell cycle and inducing a prolonged transit in G1 phase. Affects cell proliferation probably by repressing translation of specific mRNAs. Maintains the germ cell lineage by suppressing both Bax-dependent and -independent apoptotic pathways. Essential in the early stage embryo to protect the migrating primordial germ cells (PGCs) from apoptosis.

**Summary**, from NCBI Gene [342977](https://www.ncbi.nlm.nih.gov/gene/342977):

> Enables enzyme activator activity. Involved in germ cell development; mRNA destabilization; and negative regulation of translation. Located in cytosol; nucleoplasm; and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22048](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22048) · Entrez [342977](https://www.ncbi.nlm.nih.gov/gene/342977) · UniProt [P60323](https://www.uniprot.org/uniprotkb/P60323) · Ensembl [ENSG00000187556](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187556)

## Data

Gene col 11923: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11923); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11923, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11923]; `tensor/DDL_lfc|DDL_z.npy` [11923]; `embed/gene_vectors.npy` [11923]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11923 or target_col == 11923). Every well: [[NANOS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NANOS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
