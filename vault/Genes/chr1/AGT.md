---
symbol: "AGT"
type: "gene"
col: 5750
ensembl_id: "ENSG00000135744"
name: "angiotensinogen"
location: "1q42.2"
module: 8
arm: "+"
pooled_cpm: 3.63
n_lines_expressing: 17
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 10
direction_downstream: 18
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# AGT

*angiotensinogen* — 1q42.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 7.03× (z +11.3, q 7e-27, up in 5 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.24× (z +9.6, q 1e-19, up in 4 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.522× (z -3.8, q 0.056, down in 7 of 12 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SHP-77 0.0240×, HepG2/C3A 0.131×; ⚠ cell-cycle shift, explains ~46% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SHP-77 0.0354×, HepG2/C3A 0.175×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (SHP-77 0.140×); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.203×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFI]] (+0.65, fdr 1e-05), [[HLA-DRA]] (+0.64, fdr 1e-05), [[HLA-DRB1]] (+0.61, fdr 3e-05); moves opposite to [[PITHD1]] (-0.45, fdr 1e-04), [[HMGA1]] (-0.45, fdr 2e-04), [[INO80E]] (-0.44, fdr 5e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[CALCA]] → it (grade C ⚠); 18 go from it, the strongest it → [[CTSD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5750.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.03×** | +11.3 | 7e-27 | 5/5 (HepG2/C3A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.96×** | +10.8 | 9e-25 | 3/4 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.24×** | +9.6 | 1e-19 | 4/10 (A498, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.83×** | +9.5 | 5e-19 | 4/4 (SHP-77, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.75×** | +4.6 | 5e-04 | 7/13 (NCI-H2347, HepG2/C3A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.11×** | +4.3 | 0.002 | 0/9 | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.74×** | +4.2 | 0.002 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.95×** | +4.2 | 0.002 | 1/3 (HepG2/C3A) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.00×** | +4.0 | 0.004 | 1/2 (HepG2/C3A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +3.9 | 0.005 | 0/12 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.4 | 0.034 | 1/3 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.3 | 0.049 | 2/14 (A498, HepG2/C3A) | top dose only |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.74×** | +3.2 | 0.062 | 0/7 | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.84×** | +3.2 | 0.063 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.70×** | +3.1 | 0.080 | 2/6 (SHP-77, HepG2/C3A) | inconsistent across doses | cell-cycle shift (explains ~4% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5750.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SHP-77 0.0240×, HepG2/C3A 0.131×; ⚠ cell-cycle shift, explains ~46% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SHP-77 0.0354×, HepG2/C3A 0.175×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (SHP-77 0.140×); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.203×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.522×** | -3.8 | 0.056 | 7/12 (HepG2/C3A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.515×** | -3.7 | 0.056 | 3/11 (SHP-77, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.539× | -3.3 | 0.16 | 4/13 (HS-578T, H4, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | 0.364× | -3.1 | 0.29 | 3/12 (HepG2/C3A, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5750. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 110 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -16.9) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.203× (z -9.0) |
| [[SHP-77 (line)]] | alt | 93.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0240× (z -31.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.140× (z -11.1) |
| [[A498 (line)]] | wt | 0.997 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +8.8) | — |
| [[A-172 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.414 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.414 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.768 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.517 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.935 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.722 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.486 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.619 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.592 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.609 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.538 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.501 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.784 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.641 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.698 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.508 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5750), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFI]] | +0.65 | +0.68 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[HLA-DRA]] | +0.64 | +0.50 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[HLA-DRB1]] | +0.61 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[AMBP]] | +0.60 | +0.65 / +0.56 | both halves | 1e-05 | STRING 612 |
| [[FGG]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 | STRING 432 |
| [[FGA]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 | STRING 459 |
| [[CPE]] | +0.54 | +0.58 / +0.40 | both halves | 5e-05 | pathway: Peptide hormone metabolism |
| [[FGL1]] | +0.53 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[CD302]] | +0.52 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[SAA4]] | +0.51 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[CD74]] | +0.51 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[KHDRBS2]] | +0.50 | +0.38 / +0.46 | both halves | 6e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PITHD1]] | -0.45 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[HMGA1]] | -0.45 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[INO80E]] | -0.44 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[STK10]] | -0.43 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[ARF6]] | -0.42 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[ZNF92]] | -0.41 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[C11orf68]] | -0.40 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[MANCR]] | -0.40 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[CDKN2AIP]] | -0.40 | -0.32 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALCA]] | C | CALCA activity raises AGT's level | lines that do not express CALCA (45) vs lines expressing it (5) | 4.86× lower at baseline in the lines without CALCA | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[AMBP]] | C | AMBP activity raises AGT's level | lines that do not express AMBP (41) vs lines expressing it (9) | 4.23× lower at baseline in the lines without AMBP | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2; co-absent with the target |
| [[CGA]] | C | CGA activity raises AGT's level | lines that do not express CGA (44) vs lines expressing it (6) | 3.58× lower at baseline in the lines without CGA | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2; co-absent with the target |
| [[H19]] | C | H19 activity raises AGT's level | lines that do not express H19 (38) vs lines expressing it (12) | 1.68× lower at baseline in the lines without H19 | 0.032 | ⚠ within organs, on part of the lines; also absent: CALCA, SYT4, CGA; co-absent with the target |
| [[SERPINF1]] | C | SERPINF1 activity raises AGT's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.85× lower at baseline in the lines without SERPINF1 | 0.033 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent; co-absent with the target |
| [[SERPINA5]] | C | SERPINA5 activity raises AGT's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 2.49× lower at baseline in the lines without SERPINA5 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546; co-absent with the target |
| [[FGG]] | C | FGG activity raises AGT's level | lines that do not express FGG (42) vs lines expressing it (8) | 4.02× lower at baseline in the lines without FGG | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB; co-absent with the target |
| [[FGL1]] | C | FGL1 activity raises AGT's level | lines that do not express FGL1 (39) vs lines expressing it (11) | 2.96× lower at baseline in the lines without FGL1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |
| [[CFI]] | C | CFI activity raises AGT's level | lines that do not express CFI (31) vs lines expressing it (19) | 2.12× lower at baseline in the lines without CFI | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1; co-absent with the target |
| [[LRG1]] | C | LRG1 activity raises AGT's level | lines that do not express LRG1 (28) vs lines expressing it (22) | 1.69× lower at baseline in the lines without LRG1 | 0.083 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 4, C 14. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSD]] | B | AGT activity raises CTSD's level | lines that do not express AGT (33) vs lines expressing it (17) | 1.97× lower at baseline in the lines without AGT | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMBP, RIT2, SOX11 |
| [[CD302]] | B | AGT activity raises CD302's level | lines that do not express AGT (33) vs lines expressing it (17) | 1.78× lower at baseline in the lines without AGT | 0.055 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMBP, RIT2, SOX11 |
| [[DIP2C-AS1]] | B | AGT activity raises DIP2C-AS1's level | lines that do not express AGT (33) vs lines expressing it (17) | 1.39× lower at baseline in the lines without AGT | 0.062 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMBP, RIT2, SOX11 |
| [[SLC19A2]] | B | AGT activity raises SLC19A2's level | lines that do not express AGT (33) vs lines expressing it (17) | 1.48× lower at baseline in the lines without AGT | 0.080 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMBP, RIT2, SOX11 |
| [[HLA-DRA]] | C | AGT activity raises HLA-DRA's level | lines that do not express AGT (33) vs lines expressing it (17) | 1.64× lower at baseline in the lines without AGT | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMBP, RIT2, SOX11; co-absent with the target |
| [[CD74]] | C | AGT activity raises CD74's level | lines that do not express AGT (33) vs lines expressing it (17) | 2.28× lower at baseline in the lines without AGT | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMBP, RIT2, SOX11; co-absent with the target |
| [[CFI]] | C | AGT activity raises CFI's level | lines that do not express AGT (33) vs lines expressing it (17) | 2.86× lower at baseline in the lines without AGT | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMBP, RIT2, SOX11; co-absent with the target |
| [[HLA-DRB1]] | C | AGT activity raises HLA-DRB1's level | lines that do not express AGT (33) vs lines expressing it (17) | 1.54× lower at baseline in the lines without AGT | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMBP, RIT2, SOX11; co-absent with the target |
| [[TNFSF14]] | C | AGT activity raises TNFSF14's level | lines that do not express AGT (33) vs lines expressing it (17) | 2.23× lower at baseline in the lines without AGT | 0.043 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMBP, RIT2, SOX11; co-absent with the target |
| [[SAA1]] | C | AGT activity raises SAA1's level | lines that do not express AGT (33) vs lines expressing it (17) | 3.08× lower at baseline in the lines without AGT | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMBP, RIT2, SOX11; co-absent with the target |
| [[SAA2]] | C | AGT activity raises SAA2's level | lines that do not express AGT (33) vs lines expressing it (17) | 2.78× lower at baseline in the lines without AGT | 0.046 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMBP, RIT2, SOX11; co-absent with the target |
| [[PKHD1]] | C | AGT activity raises PKHD1's level | lines that do not express AGT (33) vs lines expressing it (17) | 1.73× lower at baseline in the lines without AGT | 0.047 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMBP, RIT2, SOX11; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.335). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.8, 54.9); signed map (61.5, -3.0). **Vector** length 21.6, 4.14% of its response variance represented; |z| ≥ 3 in 282 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +9.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.0 | +1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.9 | +1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.8 | +2.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.6 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -0.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.0 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -0.9 | -0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.8 | +0.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -2.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.6 | -2.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | angiotensinogen |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.2 — chr1:230,690,776-230,745,576 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SERPINA8 |
| Gene groups (HGNC) | Serpin peptidase inhibitors; Neuropeptides |
| Reactome | 12 pathways, smallest: Metabolism of Angiotensinogen to Angiotensins; Peptide hormone metabolism; Peptide ligand-binding receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P01019](https://www.uniprot.org/uniprotkb/P01019) (Angiotensinogen):

> Essential component of the renin-angiotensin system (RAS), a potent regulator of blood pressure, body fluid and electrolyte homeostasis.; [Angiotensin-2]: Acts directly on vascular smooth muscle as a potent vasoconstrictor, affects cardiac contractility and heart rate through its action on the sympathetic nervous system, and alters renal sodium and water absorption through its ability to stimulate the zona glomerulosa cells of the adrenal cortex to synthesize and secrete aldosterone. Acts by …

**Summary**, from NCBI Gene [183](https://www.ncbi.nlm.nih.gov/gene/183):

> The protein encoded by this gene, pre-angiotensinogen or angiotensinogen precursor, is expressed in the liver and is cleaved by the enzyme renin in response to lowered blood pressure. The resulting product, angiotensin I, is then cleaved by angiotensin converting enzyme (ACE) to generate the physiologically active enzyme angiotensin II. The protein is involved in maintaining blood pressure, body fluid and electrolyte homeostasis, and in the pathogenesis of essential hypertension and …

**Accessions** — [HGNC:333](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:333) · Entrez [183](https://www.ncbi.nlm.nih.gov/gene/183) · UniProt [P01019](https://www.uniprot.org/uniprotkb/P01019) · Ensembl [ENSG00000135744](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135744)

## Data

Gene col 5750: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5750); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5750, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5750]; `tensor/DDL_lfc|DDL_z.npy` [5750]; `embed/gene_vectors.npy` [5750]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5750 or target_col == 5750). Every well: [[AGT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
