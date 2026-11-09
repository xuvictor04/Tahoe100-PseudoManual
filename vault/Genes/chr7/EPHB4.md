---
symbol: "EPHB4"
type: "gene"
col: 12199
ensembl_id: "ENSG00000196411"
name: "EPH receptor B4"
location: "7q22.1"
module: 77
arm: "+"
pooled_cpm: 19.95
n_lines_expressing: 48
n_dd_up: 4
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# EPHB4

*EPH receptor B4* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.35× (z +6.3, q 1e-07, up in 15 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.29× (z +5.6, q 4e-06, up in 22 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.406× (z -28.2, q 0e+00, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IMPDH1]] (+0.72, fdr 7e-06), [[BRF1]] (+0.68, fdr 1e-05), [[ZDHHC8]] (+0.68, fdr 7e-06); moves opposite to [[RIPK2-DT]] (-0.65, fdr 1e-05), [[LINC01004]] (-0.61, fdr 2e-05), [[SLC9A8]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MMP15]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RAB35]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12199.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +6.3 | 1e-07 | 15/31 (J82, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +5.7 | 4e-06 | 17/41 (NCI-H2347, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +5.6 | 4e-06 | 22/44 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.020 | 9/43 (SW480, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.15× | +3.1 | 0.23 | 14/38 (HEC-1-A, PANC-1, …) | rises with dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.10× | +3.0 | 0.24 | 4/46 (SNU-1, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12199.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.406×** | -28.2 | 0e+00 | 39/46 (LS 180, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.357×** | -21.9 | 0e+00 | 39/46 (NCI-H2347, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.444×** | -17.9 | 0e+00 | 39/45 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.719×** | -10.3 | 1e-22 | 24/45 (Hs 766T, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.645×** | -9.7 | 4e-20 | 29/46 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.650×** | -9.5 | 2e-19 | 30/44 (SNU-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.676×** | -8.5 | 2e-15 | 28/46 (HS-578T, A-172, …) | two highest doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.683×** | -8.4 | 3e-15 | 25/46 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.696×** | -7.8 | 3e-13 | 24/46 (LS 180, C32, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.719×** | -7.0 | 2e-10 | 22/44 (RPMI-7951, HS-578T, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.748×** | -6.2 | 4e-08 | 22/46 (SK-MEL-2, Hs 766T, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.766×** | -5.9 | 2e-07 | 17/46 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.771×** | -5.6 | 7e-07 | 19/45 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.615×** | -5.6 | 9e-07 | 19/46 (NCI-H460, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.845× | -5.2 | 6e-06 | 15/46 (A-172, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.796×** | -4.9 | 3e-05 | 19/46 (SNU-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12199. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 25.7 | 0 | 5 | — | [[Harringtonine (drug)]] 0.5 µM 0.164× (z -15.2) |
| [[MIA PaCa-2 (line)]] | alt | 36.5 | 0 | 5 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0912× (z -14.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.302× (z -14.7) |
| [[NCI-H460 (line)]] | wt | 16.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -13.8) |
| [[Panc 03.27 (line)]] | alt | 42.0 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -14.0) |
| [[LS 180 (line)]] | wt | 30.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -21.4) |
| [[NCI-H1573 (line)]] | alt | 16.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0501× (z -19.3) |
| [[SNU-1 (line)]] | wt | 21.1 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0710× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0857× (z -11.8) |
| [[SW480 (line)]] | alt | 15.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -12.1) |
| [[Hs 766T (line)]] | wt | 34.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -19.4) |
| [[NCI-H2347 (line)]] | alt | 25.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -17.7) |
| [[SK-MEL-2 (line)]] | alt | 21.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -20.0) |
| [[SW48 (line)]] | wt | 37.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -15.2) |
| [[AN3 CA (line)]] | alt | 65.2 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0744× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 13.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -12.4) |
| [[BT-474 (line)]] | alt | 26.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -14.4) |
| [[C-33 A (line)]] | alt | 27.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.309× (z -10.4) |
| [[C32 (line)]] | wt | 42.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.287× (z -9.5) |
| [[HOP62 (line)]] | alt | 14.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.225× (z -10.2) |
| [[HS-578T (line)]] | alt | 21.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -11.4) |
| [[LoVo (line)]] | wt | 19.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 13.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -14.9) |
| [[NCI-H2030 (line)]] | alt | 20.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -14.7) |
| [[A498 (line)]] | wt | 28.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -11.2) |
| [[H4 (line)]] | wt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -9.1) |
| [[HCT15 (line)]] | alt | 19.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -13.4) |
| [[HT-29 (line)]] | alt | 29.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -13.8) |
| [[KATO III (line)]] | alt | 30.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -16.2) |
| [[NCI-H23 (line)]] | alt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -13.6) |
| [[PANC-1 (line)]] | alt | 18.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.377× (z -10.3) |
| [[RKO (line)]] | wt | 29.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 7.93 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.106× (z -8.5) |
| [[SW 900 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.190× (z -8.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.88 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12199), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IMPDH1]] | +0.72 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[BRF1]] | +0.68 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[ZDHHC8]] | +0.68 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[LPCAT4]] | +0.67 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[PIK3R2]] | +0.67 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[AP2A2]] | +0.64 | +0.69 / +0.49 | both halves | 1e-05 | pathway: EPH-Ephrin signaling; STRING 515 |
| [[BCR]] | +0.63 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[ANKRD27]] | +0.63 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[MAST3]] | +0.63 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[PARD6G]] | +0.63 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[MMP15]] | +0.62 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[CPSF4]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIPK2-DT]] | -0.65 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[LINC01004]] | -0.61 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[SLC9A8]] | -0.61 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[ERCC6L2]] | -0.60 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[BAZ2B]] | -0.60 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[PLA2G4C]] | -0.59 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[PATL2]] | -0.58 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[AK9]] | -0.57 | -0.62 / -0.31 | both halves | 2e-04 |  |
| [[BCL2L13]] | -0.57 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[LPXN]] | -0.57 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[PPP1R12A-AS2]] | -0.56 | -0.64 / -0.30 | both halves | 2e-04 |  |
| [[PDCL3P4]] | -0.56 | -0.63 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP15]] | B | MMP15 activity raises EPHB4's level | lines that do not express MMP15 (6) vs lines expressing it (44) | 2.20× lower at baseline in the lines without MMP15 | 0.022 | ⚠ within organs, on part of the lines; also absent: RTN4R, NOXA1, PTPN3; maybe low, not absent |
| [[JAG2]] | B | JAG2 activity raises EPHB4's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.60× lower at baseline in the lines without JAG2 | 0.029 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises EPHB4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB35]] | B | EPHB4 activity raises RAB35's level | compounds that target EPHB4: 2 of 3 lower it (NG25, NVP-BHG712) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.719). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-0.4, -0.6); signed map (-41.6, -7.3). **Vector** length 85.1, 17.0% of its response variance represented; |z| ≥ 3 in 941 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.6 | +5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | -0.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.5 | +5.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -2.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | +0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -17.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -21.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.6 | -9.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -5.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | EPH receptor B4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,802,565-100,827,523 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Tyro11; previously HTK |
| Gene groups (HGNC) | Sterile alpha motif domain containing; EPH receptors |
| Hallmark sets | APICAL_SURFACE |
| Reactome | 6 pathways, smallest: Ephrin signaling; EPHB-mediated forward signaling; EPH-ephrin mediated repulsion of cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P54760](https://www.uniprot.org/uniprotkb/P54760) (Ephrin type-B receptor 4):

> Receptor tyrosine kinase which binds promiscuously to transmembrane ephrin-B family ligands residing on adjacent cells, leading to contact-dependent bidirectional signaling into neighboring cells. The signaling pathway downstream of the receptor is referred to as forward signaling while the signaling pathway downstream of the ephrin ligand is referred to as reverse signaling. Together with its cognate ligand/functional ligand EFNB2, it is involved in the regulation of cell adhesion and …

**Summary**, from NCBI Gene [2050](https://www.ncbi.nlm.nih.gov/gene/2050):

> Ephrin receptors and their ligands, the ephrins, mediate numerous developmental processes, particularly in the nervous system. Based on their structures and sequence relationships, ephrins are divided into the ephrin-A (EFNA) class, which are anchored to the membrane by a glycosylphosphatidylinositol linkage, and the ephrin-B (EFNB) class, which are transmembrane proteins. The Eph family of receptors are divided into 2 groups based on the similarity of their extracellular domain sequences and …

**Accessions** — [HGNC:3395](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3395) · Entrez [2050](https://www.ncbi.nlm.nih.gov/gene/2050) · UniProt [P54760](https://www.uniprot.org/uniprotkb/P54760) · Ensembl [ENSG00000196411](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196411)

## Data

Gene col 12199: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12199); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12199, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12199]; `tensor/DDL_lfc|DDL_z.npy` [12199]; `embed/gene_vectors.npy` [12199]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12199 or target_col == 12199). Every well: [[EPHB4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPHB4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
