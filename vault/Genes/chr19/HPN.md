---
symbol: "HPN"
type: "gene"
col: 2650
ensembl_id: "ENSG00000105707"
name: "hepsin"
location: "19q13.11"
module: 47
arm: "+"
pooled_cpm: 4.37
n_lines_expressing: 44
n_dd_up: 6
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# HPN

*hepsin* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.54× (z +10.6, q 3e-23, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +4.0, q 0.010, up in 3 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.314× (z -10.1, q 3e-21, down in 23 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCN1B]] (+0.69, fdr 7e-06, ⚠ same locus), [[F2]] (+0.67, fdr 1e-05), [[LINC01277]] (+0.65, fdr 7e-06), [[SPON2]] (+0.65, fdr 1e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LSMEM2]] → it (grade B ⚠); 4 go from it, the strongest it → [[SLC8A2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2650.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.54×** | +10.6 | 3e-23 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.30×** | +7.2 | 1e-10 | 1/10 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +5.5 | 9e-06 | 1/5 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.010 | 3/25 (A549, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.56×** | +3.9 | 0.013 | 8/40 (A498, SW 900, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.070 | 7/36 (A498, HOP62, …) | top dose only | position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.42× | +3.0 | 0.22 | 3/21 (SW480, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2650.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.314×** | -10.1 | 3e-21 | 23/40 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.419×** | -7.6 | 9e-12 | 19/38 (HT-29, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.475×** | -6.5 | 1e-08 | 23/36 (HepG2/C3A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.511×** | -5.9 | 6e-07 | 18/35 (SW480, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.609×** | -4.3 | 0.002 | 10/36 (A498, HepG2/C3A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.641×** | -3.9 | 0.009 | 15/39 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.647×** | -3.8 | 0.011 | 11/40 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.653×** | -3.7 | 0.013 | 13/18 (HepG2/C3A, SW480, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Erlotinib (drug)]] 5 µM |  | **0.645×** | -3.7 | 0.014 | 14/33 (CFPAC-1, A498, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.451×** | -3.6 | 0.015 | 5/21 (HepG2/C3A, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.658×** | -3.5 | 0.028 | 7/28 (HEC-1-A, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.679×** | -3.3 | 0.049 | 12/35 (SW480, NCI-H2347, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.690×** | -3.3 | 0.049 | 10/38 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.692×** | -3.2 | 0.049 | 5/39 (LOX-IMVI, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2650. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 125 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -9.1) |
| [[HT-29 (line)]] | alt | 4.21 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0389× (z -14.0) |
| [[SW480 (line)]] | alt | 4.14 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0864× (z -9.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.623 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.827 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.933 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2650), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCN1B]] | +0.69 | +0.73 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; ⚠ same locus (0.1 kb, same strand: neighbours can correlate without regulation) |
| [[F2]] | +0.67 | +0.67 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_COAGULATION |
| [[LINC01277]] | +0.65 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[SPON2]] | +0.65 | +0.66 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[GAL3ST2]] | +0.65 | +0.62 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[C19orf38]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[MYO15A]] | +0.64 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[MROH3P]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[GAL3ST1]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[SGSM3-AS1]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[TNFSF14]] | +0.62 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[TMEM25]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LSMEM2]] | B | LSMEM2 activity raises HPN's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 1.74× lower at baseline in the lines without LSMEM2 | 0.036 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[SCUBE2]] | B | SCUBE2 activity lowers HPN's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 1.12× higher at baseline in the lines without SCUBE2 | 0.071 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[PTPN6]] | B | PTPN6 activity raises HPN's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.43× lower at baseline in the lines without PTPN6 | 0.072 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |
| [[BTBD16]] | B | BTBD16 activity lowers HPN's level | lines that do not express BTBD16 (11) vs lines expressing it (39) | 1.21× higher at baseline in the lines without BTBD16 | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MROH3P]] | B | MROH3P activity raises HPN's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 1.59× lower at baseline in the lines without MROH3P | 0.082 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC8A2]] | B | HPN activity raises SLC8A2's level | lines that do not express HPN (6) vs lines expressing it (44) | 2.08× lower at baseline in the lines without HPN | 0.048 | ⚠ within organs, on part of the lines; also absent: NAT14, APBA1; maybe low, not absent |
| [[PTPN6]] | B | HPN activity raises PTPN6's level | lines that do not express HPN (6) vs lines expressing it (44) | 1.84× lower at baseline in the lines without HPN | 0.058 | ⚠ within organs, on part of the lines; also absent: NAT14, APBA1; maybe low, not absent |
| [[FSCN2]] | B | HPN activity raises FSCN2's level | lines that do not express HPN (6) vs lines expressing it (44) | 1.47× lower at baseline in the lines without HPN | 0.076 | ⚠ within organs, on part of the lines; also absent: NAT14, APBA1; maybe low, not absent |
| [[PYGM]] | B | HPN activity raises PYGM's level | lines that do not express HPN (6) vs lines expressing it (44) | 1.58× lower at baseline in the lines without HPN | 0.096 | ⚠ within organs, on part of the lines; also absent: NAT14, APBA1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.668). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.5, -17.2); signed map (19.0, 13.6). **Vector** length 63.7, 10.7% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +3.9 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -10.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -6.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.2 | -5.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.2 | -1.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.9 | -3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | hepsin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:35,040,506-35,066,573 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TMPRSS1 |
| Gene groups (HGNC) | Scavenger receptor cysteine rich domain containing; Type II transmembrane serine proteases |
| Hallmark sets | COAGULATION, INFLAMMATORY_RESPONSE |
| Reactome | 4 pathways, smallest: Signaling by MST1; MET Receptor Activation; Signaling by MET |
| Matched by | ensembl_id |

**Function**, from UniProt [P05981](https://www.uniprot.org/uniprotkb/P05981) (Serine protease hepsin):

> Serine protease that cleaves extracellular substrates, and contributes to the proteolytic processing of growth factors, such as HGF and MST1/HGFL. Plays a role in cell growth and maintenance of cell morphology. Plays a role in the proteolytic processing of ACE2. Mediates the proteolytic cleavage of urinary UMOD that is required for UMOD polymerization.

**Summary**, from NCBI Gene [3249](https://www.ncbi.nlm.nih.gov/gene/3249):

> This gene encodes a type II transmembrane serine protease that may be involved in diverse cellular functions, including blood coagulation and the maintenance of cell morphology. Expression of the encoded protein is associated with the growth and progression of cancers, particularly prostate cancer. The protein is cleaved into a catalytic serine protease chain and a non-catalytic scavenger receptor cysteine-rich chain, which associate via a single disulfide bond. Alternative splicing results in …

**Accessions** — [HGNC:5155](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5155) · Entrez [3249](https://www.ncbi.nlm.nih.gov/gene/3249) · UniProt [P05981](https://www.uniprot.org/uniprotkb/P05981) · Ensembl [ENSG00000105707](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105707)

## Data

Gene col 2650: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2650); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2650, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2650]; `tensor/DDL_lfc|DDL_z.npy` [2650]; `embed/gene_vectors.npy` [2650]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2650 or target_col == 2650). Every well: [[HPN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HPN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
