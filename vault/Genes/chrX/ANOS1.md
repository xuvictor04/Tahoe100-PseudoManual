---
symbol: "ANOS1"
type: "gene"
col: 228
ensembl_id: "ENSG00000011201"
name: "anosmin 1"
location: "Xp22.31"
module: 152
arm: "+"
pooled_cpm: 3.43
n_lines_expressing: 19
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# ANOS1

*anosmin 1* — Xp22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.09× (z +16.2, q 0e+00, up in 6 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 3.36× (z +15.4, q 0e+00, up in 15 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.130×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-423 0.235×); [[Docetaxel (drug)]] 0.05 µM in 1 line (Panc 03.27 0.155×; ⚠ transcription drop).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDGFD]] (+0.64, fdr 1e-05), [[GUCY1B1]] (+0.62, fdr 1e-05), [[ZMAT4]] (+0.61, fdr 3e-05); moves opposite to [[RECQL5]] (-0.61, fdr 1e-05), [[KRIT1]] (-0.56, fdr 6e-05), [[ADPRHL1]] (-0.55, fdr 2e-04).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NXPH4]] → it (grade B ⚠); 3 go from it, the strongest it → [[NR3C2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 228.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.09×** | +16.2 | 0e+00 | 6/10 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **3.36×** | +15.4 | 0e+00 | 15/15 (HS-578T, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.18×** | +14.2 | 2e-43 | 6/8 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.57×** | +12.6 | 2e-34 | 2/8 (Panc 03.27, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.67×** | +11.6 | 3e-29 | 15/15 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.14×** | +10.3 | 8e-23 | 15/15 (NCI-H1792, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.60×** | +8.6 | 8e-16 | 15/15 (NCI-H1792, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +8.3 | 8e-15 | 2/13 (HEC-1-A, A-172) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.39×** | +7.8 | 4e-13 | 14/15 (NCI-H1792, J82, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.26×** | +7.3 | 1e-11 | 13/14 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +6.9 | 4e-10 | 1/13 (A-172) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +6.4 | 5e-09 | 3/13 (BT-474, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +5.8 | 3e-07 | 1/11 (HEC-1-A) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +5.4 | 3e-06 | 6/15 (A-172, BT-474, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.6 | 1e-04 | 5/15 (HEC-1-A, BT-474, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.16×** | +3.6 | 0.008 | 15/15 (NCI-H1792, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.019 | 1/12 (HEC-1-A) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.62×** | +3.1 | 0.042 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.61×** | +3.1 | 0.046 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.060 | 4/15 (HS-578T, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 228.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.130×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-423 0.235×); [[Docetaxel (drug)]] 0.05 µM in 1 line (Panc 03.27 0.155×; ⚠ transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | 0.704× | -3.1 | 0.91 | 3/15 (HS-578T, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 228. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 11.5 | 5 | 1 | [[Panobinostat (drug)]] 0.5 µM 11.9× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -12.6) |
| [[BT-474 (line)]] | alt | 18.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 5.06 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.56× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 6.76 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.38× (z +9.4) | — |
| [[J82 (line)]] | alt | 6.85 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 10.1× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.155× (z -10.7) ⚠ transcription drop |
| [[SNU-423 (line)]] | alt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -11.0) |
| [[A-172 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.765 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.845 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.429 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.941 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.605 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.514 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.557 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.458 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.498 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.514 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.406 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.473 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.424 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 228), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDGFD]] | +0.64 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[GUCY1B1]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[ZMAT4]] | +0.61 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[PKIA]] | +0.60 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[TMEM108]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[COLEC12]] | +0.58 | +0.40 / +0.71 | both halves | 4e-05 |  |
| [[CPA4]] | +0.58 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[PLCXD2]] | +0.58 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[LPCAT2]] | +0.58 | +0.30 / +0.59 | both halves | 2e-04 |  |
| [[TRAK1]] | +0.57 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[RAB3B]] | +0.57 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[GLRB]] | +0.57 | +0.42 / +0.62 | both halves | 4e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RECQL5]] | -0.61 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[KRIT1]] | -0.56 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[ADPRHL1]] | -0.55 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[UBE3B]] | -0.53 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[SENP8]] | -0.52 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[NMNAT1]] | -0.51 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[PEF1]] | -0.51 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[ACAD9]] | -0.51 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[PAAF1]] | -0.49 | -0.24 / -0.44 | both halves | 5e-04 |  |
| [[RPAP1]] | -0.49 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[RPRD1B]] | -0.48 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[PPP5D1P-1]] | -0.48 | -0.29 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NXPH4]] | B | NXPH4 activity lowers ANOS1's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 1.84× higher at baseline in the lines without NXPH4 | 0.027 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C2]] | B | ANOS1 activity raises NR3C2's level | lines that do not express ANOS1 (31) vs lines expressing it (19) | 1.97× lower at baseline in the lines without ANOS1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000268119, ZYG11A, KRT7 |
| [[LPCAT2]] | B | ANOS1 activity raises LPCAT2's level | lines that do not express ANOS1 (31) vs lines expressing it (19) | 1.34× lower at baseline in the lines without ANOS1 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000268119, ZYG11A, KRT7 |
| [[ADPRHL1]] | B | ANOS1 activity raises ADPRHL1's level | lines that do not express ANOS1 (31) vs lines expressing it (19) | 1.84× lower at baseline in the lines without ANOS1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000268119, ZYG11A, KRT7 |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.399). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.0, 31.4); signed map (33.8, 33.6). **Vector** length 34.3, 7.38% of its response variance represented; |z| ≥ 3 in 399 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +15.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +16.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +12.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.8 | +1.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +0.8 | +2.2 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -0.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -2.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | anosmin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.31 — chrX:8,528,874-8,732,137 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KALIG-1, WFDC19; previously KAL, ADMLX, KAL1 |
| Gene groups (HGNC) | WAP four-disulfide core domain containing; Fibronectin type III domain containing |
| Reactome | 6 pathways, smallest: FGFR1 ligand binding and activation; FGFR1c ligand binding and activation; Negative regulation of FGFR1 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P23352](https://www.uniprot.org/uniprotkb/P23352) (Anosmin-1):

> Has a dual branch-promoting and guidance activity, which may play an important role in the patterning of mitral and tufted cell collaterals to the olfactory cortex (By similarity). Chemoattractant for fetal olfactory epithelial cells.

**Summary**, from NCBI Gene [3730](https://www.ncbi.nlm.nih.gov/gene/3730):

> Mutations in this gene cause the X-linked Kallmann syndrome. The encoded protein is similar in sequence to proteins known to function in neural cell adhesion and axonal migration. In addition, this cell surface protein is N-glycosylated and may have anti-protease activity. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6211](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6211) · Entrez [3730](https://www.ncbi.nlm.nih.gov/gene/3730) · UniProt [P23352](https://www.uniprot.org/uniprotkb/P23352) · Ensembl [ENSG00000011201](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011201)

## Data

Gene col 228: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 228); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 228, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 228]; `tensor/DDL_lfc|DDL_z.npy` [228]; `embed/gene_vectors.npy` [228]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 228 or target_col == 228). Every well: [[ANOS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANOS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
