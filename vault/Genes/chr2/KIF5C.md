---
symbol: "KIF5C"
type: "gene"
col: 9624
ensembl_id: "ENSG00000168280"
name: "kinesin family member 5C"
location: "2q23.1-q23.2"
module: 82
arm: "+"
pooled_cpm: 22.7
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 9
n_dd_up_clean: 20
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# KIF5C

*kinesin family member 5C* — 2q23.1-q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.07× (z +24.0, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Glycyrrhizic acid (drug)]] 0.5 µM: 0.674× (z -6.3, q 1e-07, down in 20 of 47 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRS]] (+0.68, fdr 1e-05), [[NOVA2]] (+0.65, fdr 7e-06), [[APBA1]] (+0.64, fdr 9e-06); moves opposite to [[SPART-AS1]] (-0.52, fdr 3e-05), [[INTS14]] (-0.49, fdr 6e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CRMP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9624.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.07×** | +24.0 | 0e+00 | 42/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.41×** | +23.8 | 0e+00 | 35/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.38×** | +23.7 | 0e+00 | 34/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.16×** | +18.4 | 0e+00 | 33/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.49×** | +14.6 | 0e+00 | 33/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.39×** | +13.4 | 9e-39 | 33/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +12.3 | 5e-33 | 25/32 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +10.8 | 4e-25 | 31/43 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.93×** | +9.0 | 1e-17 | 28/48 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +8.5 | 2e-15 | 28/47 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +7.8 | 3e-13 | 21/38 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +7.0 | 1e-10 | 25/47 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.52×** | +6.4 | 8e-09 | 27/47 (HepG2/C3A, NCI-H460, …) | rises with dose | position effect removed |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.42×** | +5.6 | 7e-07 | 23/48 (AsPC-1, LoVo, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.004 | 12/47 (HS-578T, PANC-1, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.006 | 12/48 (NCI-H460, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.007 | 12/48 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Pralsetinib (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.016 | 6/48 (LoVo, RKO, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9624.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.674×** | -6.3 | 1e-07 | 20/47 (SHP-77, A-172, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Penfluridol (drug)]] 0.5 µM |  | **0.750×** | -4.6 | 1e-03 | 17/47 (C-33 A, SHP-77, …) | two highest doses | position effect removed |
| [[Pimozide (drug)]] 5 µM |  | **0.771×** | -4.2 | 0.005 | 13/48 (A-172, SHP-77, …) | top dose only | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.774×** | -4.1 | 0.005 | 15/48 (A-172, J82, …) | inconsistent across doses | position effect removed |
| [[Artemether (drug)]] 5 µM |  | **0.794×** | -3.7 | 0.021 | 11/48 (A-172, A-427, …) | top dose only | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.821×** | -3.7 | 0.022 | 15/48 (A-172, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Penfluridol (drug)]] 5 µM |  | **0.791×** | -3.6 | 0.022 | 13/47 (A-427, A-172, …) | two highest doses | position effect removed |
| [[Adenosine (drug)]] 5 µM |  | 0.839× | -3.6 | 0.022 | 9/48 (SW480, A-172, …) | top dose only | position effect removed |
| [[Furosemide (drug)]] 0.5 µM |  | **0.806×** | -3.5 | 0.031 | 9/48 (SW 1271, LOX-IMVI, …) | rises with dose | position effect removed |
| [[OTS514 (drug)]] 0.5 µM |  | **0.747×** | -3.4 | 0.043 | 8/48 (A-172, A-427, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Furosemide (drug)]] 5 µM |  | 0.856× | -3.3 | 0.043 | 7/48 (HOP62, PANC-1, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9624. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.3 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 8.76× (z +20.5) | — |
| [[PANC-1 (line)]] | alt | 12.6 | 7 | 0 | [[Panobinostat (drug)]] 0.5 µM 13.0× (z +19.0) | — |
| [[HOP62 (line)]] | alt | 22.7 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 4.58× (z +14.6) | — |
| [[J82 (line)]] | alt | 33.5 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 3.89× (z +11.5) | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 7.71× (z +13.0) | — |
| [[SW480 (line)]] | alt | 10.4 | 6 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 6.20× (z +16.5) | — |
| [[A549 (line)]] | wt | 19.1 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 4.49× (z +12.3) | — |
| [[BT-474 (line)]] | alt | 21.5 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 4.30× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 24.3 | 4 | 1 | [[Panobinostat (drug)]] 0.5 µM 5.10× (z +11.2) | [[Hydroxyurea (drug)]] 0.05 µM 0.225× (z -9.4) |
| [[SNU-423 (line)]] | alt | 10.5 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 7.51× (z +12.9) | — |
| [[SW 900 (line)]] | alt | 22.3 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 9.75× (z +13.0) | — |
| [[A498 (line)]] | wt | 10.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 9.57× (z +14.2) | — |
| [[LOX-IMVI (line)]] | wt | 19.3 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 4.44× (z +13.4) | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 12.0× (z +13.4) | — |
| [[hTERT-HPNE (line)]] | wt | 29.8 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 4.59× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 12.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.06× (z +9.4) | — |
| [[C32 (line)]] | wt | 10.3 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.32× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 9.75 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.54× (z +9.9) | — |
| [[HCT15 (line)]] | alt | 21.2 | 0 | 2 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0492× (z -9.8) |
| [[LoVo (line)]] | wt | 9.65 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.41× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 10.6 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 8.45× (z +13.9) | — |
| [[A-427 (line)]] | wt | 75.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 11.6 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.137× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 14.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.23× (z +8.6) | — |
| [[A-172 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 111 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9624), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRS]] | +0.68 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[NOVA2]] | +0.65 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[APBA1]] | +0.64 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[MAP6]] | +0.64 | +0.46 / +0.66 | both halves | 2e-05 |  |
| [[CACNG7]] | +0.62 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ATP1A3]] | +0.62 | +0.36 / +0.72 | both halves | 1e-04 |  |
| [[MAST1]] | +0.61 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[KIF5A]] | +0.61 | +0.50 / +0.67 | both halves | 1e-05 | same gene group; pathway: Affinity selection of immunoglobulins; STRING 965 |
| [[VAT1L]] | +0.60 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[CRLF1]] | +0.60 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[SLC29A4]] | +0.60 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[SLC17A7]] | +0.59 | +0.48 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPART-AS1]] | -0.52 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[INTS14]] | -0.49 | -0.22 / -0.58 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRMP1]] | B | CRMP1 activity raises KIF5C's level | lines that do not express CRMP1 (19) vs lines expressing it (31) | 2.02× lower at baseline in the lines without CRMP1 | 0.097 | ⚠ within organs, on part of the lines; also absent: JAM3, NHSL2, ENSG00000286033; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.721). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.7, 39.2); signed map (27.4, 29.2). **Vector** length 73.4, 12.6% of its response variance represented; |z| ≥ 3 in 1,048 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +11.5 | +24.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.9 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.8 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.7 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +7.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.6 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +9.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +2.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.4 | -0.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.8 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.3 | +0.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.2 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | +0.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 5C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q23.1-q23.2 — chr2:148,875,227-149,026,759 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NKHC2 |
| Gene groups (HGNC) | Kinesins |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 15 pathways, smallest: Insulin processing; Kinesins; Peptide hormone metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O60282](https://www.uniprot.org/uniprotkb/O60282) (Kinesin heavy chain isoform 5C):

> Microtubule-associated force-producing protein that may play a role in organelle transport. Has ATPase activity (By similarity). Involved in synaptic transmission. Mediates dendritic trafficking of mRNAs (By similarity). Required for anterograde axonal transportation of MAPK8IP3/JIP3 which is essential for MAPK8IP3/JIP3 function in axon elongation (By similarity).

**Summary**, from NCBI Gene [3800](https://www.ncbi.nlm.nih.gov/gene/3800):

> The protein encoded by this gene is a kinesin heavy chain subunit involved in the transport of cargo within the central nervous system. The encoded protein, which acts as a tetramer by associating with another heavy chain and two light chains, interacts with protein kinase CK2. Mutations in this gene have been associated with complex cortical dysplasia with other brain malformations-2. Two transcript variants, one protein-coding and the other non-protein coding, have been found for this gene. …

**Accessions** — [HGNC:6325](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6325) · Entrez [3800](https://www.ncbi.nlm.nih.gov/gene/3800) · UniProt [O60282](https://www.uniprot.org/uniprotkb/O60282) · Ensembl [ENSG00000168280](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168280)

## Data

Gene col 9624: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9624); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9624, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9624]; `tensor/DDL_lfc|DDL_z.npy` [9624]; `embed/gene_vectors.npy` [9624]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9624 or target_col == 9624). Every well: [[KIF5C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF5C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
