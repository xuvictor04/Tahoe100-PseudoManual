---
symbol: "METRNL"
type: "gene"
col: 10756
ensembl_id: "ENSG00000176845"
name: "meteorin like, glial cell differentiation regulator"
location: "17q25.3"
module: 218
arm: "+"
pooled_cpm: 14.98
n_lines_expressing: 44
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 10
direction_downstream: 1
tags: ["gene", "module/218"]
generated_by: "tahoemap"
---

# METRNL

*meteorin like, glial cell differentiation regulator* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.77× (z +9.5, q 1e-18, up in 23 of 37 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.74× (z +6.5, q 2e-08, up in 23 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Anethole trithione (drug)]] 0.5 µM: 0.725× (z -3.8, q 0.091, down in 13 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (HOP62 0.180×, HS-578T 0.214×, RPMI-7951 0.210×, hTERT-HPNE 0.295×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.0351×, HOP62 0.232×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (HOP62 0.231×, A-172 0.401×); [[Thymopentin (drug)]] 5 µM in 1 line (BT-474 0.0704×); [[Verteporfin (drug)]] 5 µM in 1 line (hTERT-HPNE 0.281×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLGAP4]] (+0.65, fdr 1e-05), [[RBM38]] (+0.64, fdr 9e-06), [[SPATA2L]] (+0.63, fdr 1e-05); moves opposite to [[PTGR2]] (-0.61, fdr 1e-05), [[TMEM123]] (-0.59, fdr 1e-05), [[FUCA2]] (-0.58, fdr 3e-05).
> It is in [[Module 218]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[LINC01615]] → it (grade B ⚠); 1 goes from it, the strongest it → [[UNC5B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10756.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.77×** | +9.5 | 1e-18 | 23/37 (COLO 205, AsPC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.74×** | +6.5 | 2e-08 | 23/41 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.56×** | +5.2 | 3e-05 | 18/38 (RPMI-7951, A-172, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +5.1 | 4e-05 | 18/39 (SW480, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +4.9 | 1e-04 | 17/40 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.92×** | +4.2 | 0.003 | 13/34 (A-172, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.007 | 14/40 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.007 | 15/41 (SW480, Panc 03.27, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.81×** | +3.8 | 0.009 | 8/39 (HOP62, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.029 | 11/41 (HS-578T, H4, …) | rises with dose | position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.053 | 14/39 (CFPAC-1, HOP62, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.055 | 9/41 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.68×** | +3.2 | 0.063 | 3/32 (LoVo, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.61×** | +3.1 | 0.087 | 4/39 (SK-MEL-2, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.60×** | +3.0 | 0.100 | 4/39 (COLO 205, KATO III, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10756.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (HOP62 0.180×, HS-578T 0.214×, RPMI-7951 0.210×, hTERT-HPNE 0.295×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.0351×, HOP62 0.232×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (HOP62 0.231×, A-172 0.401×); [[Thymopentin (drug)]] 5 µM in 1 line (BT-474 0.0704×); [[Verteporfin (drug)]] 5 µM in 1 line (hTERT-HPNE 0.281×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.725×** | -3.8 | 0.091 | 13/42 (HOP62, CFPAC-1, …) | all doses, flat |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.730× | -3.4 | 0.15 | 8/41 (LoVo, Hs 766T, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.734× | -3.4 | 0.15 | 8/40 (BT-474, SW1417, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10756. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 76.2 | 0 | 10 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -18.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.231× (z -16.0) |
| [[HS-578T (line)]] | alt | 46.4 | 0 | 7 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -15.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 55.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -13.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.401× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 75.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.281× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 51.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0351× (z -22.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 7.50 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +8.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[BT-474 (line)]] | alt | 6.31 | 0 | 1 | — | [[Thymopentin (drug)]] 5 µM 0.0704× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 9.24 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +8.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[COLO 205 (line)]] | alt | 14.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +8.8) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[J82 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.408× (z -8.7) ⚠ cell-cycle shift, explains ~81% of this change |
| [[KATO III (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.167× (z -15.0) ⚠ cell-cycle shift, explains ~81% of this change |
| [[SW1417 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.141× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.74 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10756), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLGAP4]] | +0.65 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[RBM38]] | +0.64 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[SPATA2L]] | +0.63 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[NAGK]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ASL]] | +0.61 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[PRKCD]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[PLIN3]] | +0.60 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[CDC34]] | +0.60 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[LRRC8E]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[PMM1]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[CDKN1C]] | +0.59 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[TNNT1]] | +0.59 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTGR2]] | -0.61 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[TMEM123]] | -0.59 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[FUCA2]] | -0.58 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[XRCC5]] | -0.57 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[TMX3]] | -0.57 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[CAPRIN1]] | -0.57 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[TMX1]] | -0.56 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[RBBP4]] | -0.56 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[IPO8]] | -0.55 | -0.42 / -0.70 | both halves | 4e-05 |  |
| [[SRP9]] | -0.54 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[RPE]] | -0.54 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[SUMO3]] | -0.54 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01615]] | B | LINC01615 activity raises METRNL's level | lines that do not express LINC01615 (36) vs lines expressing it (14) | 3.36× lower at baseline in the lines without LINC01615 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ENSG00000222032, GYPC |
| [[GFPT2]] | B | GFPT2 activity raises METRNL's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 1.84× lower at baseline in the lines without GFPT2 | 0.012 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |
| [[TMEM92-AS1]] | B | TMEM92-AS1 activity raises METRNL's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 2.32× lower at baseline in the lines without TMEM92-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| [[SRRM3]] | B | SRRM3 activity lowers METRNL's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 2.33× higher at baseline in the lines without SRRM3 | 0.020 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |
| [[CA12]] | B | CA12 activity raises METRNL's level | lines that do not express CA12 (29) vs lines expressing it (21) | 2.00× lower at baseline in the lines without CA12 | 0.027 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1 |
| [[BICDL1]] | B | BICDL1 activity lowers METRNL's level | lines that do not express BICDL1 (12) vs lines expressing it (38) | 2.40× higher at baseline in the lines without BICDL1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ABLIM2, KRT18, LINC00857 |
| [[TNS1]] | B | TNS1 activity raises METRNL's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 2.12× lower at baseline in the lines without TNS1 | 0.040 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[FAM167A]] | B | FAM167A activity raises METRNL's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 1.72× lower at baseline in the lines without FAM167A | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[SRRM3]] | B | SRRM3 activity strengthens METRNL's drug response | lines that do not express SRRM3 (16) vs lines expressing it (26) | the lines without SRRM3 respond 0.47× as strongly (z diff +1.03); strongest at Panobinostat 5 µM: 1.03x vs 1.93x (z diff +2.9) | 0.081 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[GPR173]] | B | GPR173 activity raises METRNL's level | lines that do not express GPR173 (30) vs lines expressing it (20) | 2.01× lower at baseline in the lines without GPR173 | 0.093 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UNC5B]] | B | METRNL activity raises UNC5B's level | lines that do not express METRNL (6) vs lines expressing it (44) | 2.79× lower at baseline in the lines without METRNL | 0.055 | ⚠ within organs, on part of the lines; also absent: FAM219A, DENND2B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 218]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.788). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.8, 1.2); signed map (-26.7, 15.8). **Vector** length 94.0, 22.7% of its response variance represented; |z| ≥ 3 in 740 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.6 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +5.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +1.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.3 | +2.8 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.1 | -3.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -2.0 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.0 | -3.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.9 | -3.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | meteorin like, glial cell differentiation regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:83,079,609-83,095,122 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q641Q3](https://www.uniprot.org/uniprotkb/Q641Q3) (Meteorin-like protein):

> Hormone induced following exercise or cold exposure that promotes energy expenditure. Induced either in the skeletal muscle after exercise or in adipose tissue following cold exposure and is present in the circulation. Able to stimulate energy expenditure associated with the browning of the white fat depots and improves glucose tolerance. Does not promote an increase in a thermogenic gene program via direct action on adipocytes, but acts by stimulating several immune cell subtypes to enter the …

**Summary**, from NCBI Gene [284207](https://www.ncbi.nlm.nih.gov/gene/284207):

> Predicted to enable hormone activity. Predicted to be involved in several processes, including brown fat cell differentiation; positive regulation of brown fat cell differentiation; and response to muscle activity. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27584](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27584) · Entrez [284207](https://www.ncbi.nlm.nih.gov/gene/284207) · UniProt [Q641Q3](https://www.uniprot.org/uniprotkb/Q641Q3) · Ensembl [ENSG00000176845](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176845)

## Data

Gene col 10756: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10756); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10756, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10756]; `tensor/DDL_lfc|DDL_z.npy` [10756]; `embed/gene_vectors.npy` [10756]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10756 or target_col == 10756). Every well: [[METRNL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METRNL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
