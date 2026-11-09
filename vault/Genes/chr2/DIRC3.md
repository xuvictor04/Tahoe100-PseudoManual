---
symbol: "DIRC3"
type: "gene"
col: 13806
ensembl_id: "ENSG00000231672"
name: "disrupted in renal carcinoma 3"
location: "2q35"
module: 66
arm: "+"
pooled_cpm: 19.83
n_lines_expressing: 31
n_dd_up: 8
n_dd_down: 38
n_dd_up_clean: 8
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 22
direction_downstream: 24
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# DIRC3

*disrupted in renal carcinoma 3* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.65× (z +8.4, q 3e-14, up in 18 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (15 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.347× (z -12.4, q 1e-32, down in 25 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMP3]] (+0.64, fdr 7e-06), [[MIR3681HG]] (+0.64, fdr 1e-05), [[SYN3]] (+0.63, fdr 1e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[CARMN]] → it (grade B ⚠); 24 go from it, the strongest it → [[MTCP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13806.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +8.4 | 3e-14 | 18/29 (A498, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.88×** | +7.5 | 2e-11 | 19/29 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.54×** | +4.9 | 2e-04 | 10/28 (A-172, H4, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +4.5 | 8e-04 | 15/28 (A-172, H4, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.4 | 0.001 | 5/29 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.41×** | +4.1 | 0.004 | 13/28 (LoVo, H4, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +4.0 | 0.006 | 8/29 (HEC-1-A, BT-474, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.057 | 2/28 (RPMI-7951, HepG2/C3A) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.29× | +3.1 | 0.13 | 13/29 (A549, RPMI-7951, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.27× | +3.0 | 0.14 | 11/29 (A-172, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 1.29× | +3.0 | 0.14 | 3/29 (SHP-77, CHP-212, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13806.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.347×** | -12.4 | 1e-32 | 25/29 (SHP-77, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.349×** | -12.3 | 2e-32 | 26/29 (SHP-77, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.380×** | -10.9 | 2e-25 | 23/28 (C32, SHP-77, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.423×** | -10.1 | 1e-21 | 24/28 (SHP-77, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.454×** | -9.3 | 2e-18 | 23/28 (C32, HT-29, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.488×** | -8.4 | 4e-15 | 23/28 (RPMI-7951, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.500×** | -8.1 | 4e-14 | 21/28 (SHP-77, C32, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.672×** | -6.5 | 4e-09 | 20/28 (SHP-77, HT-29, …) | two highest doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.583×** | -6.1 | 9e-08 | 22/27 (HepG2/C3A, RPMI-7951, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.607×** | -5.8 | 3e-07 | 18/28 (HepG2/C3A, HT-29, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.626×** | -5.5 | 2e-06 | 19/29 (NCI-H1792, CHP-212, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.629×** | -5.0 | 2e-05 | 18/29 (HT-29, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.642×** | -5.0 | 3e-05 | 19/28 (SHP-77, HT-29, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.666×** | -4.7 | 9e-05 | 15/29 (RPMI-7951, C32, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.673×** | -4.6 | 2e-04 | 16/29 (SK-MEL-2, HS-578T, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.771×** | -4.3 | 7e-04 | 16/29 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.782×** | -4.0 | 0.002 | 12/29 (HT-29, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.714×** | -3.9 | 0.003 | 10/28 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.721×** | -3.8 | 0.004 | 8/28 (SHP-77, NCI-H1792, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.563×** | -3.5 | 0.011 | 14/29 (C32, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **0.808×** | -3.5 | 0.011 | 12/30 (C32, A498, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13806. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 134 | 0 | 17 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0370× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0455× (z -15.8) |
| [[SHP-77 (line)]] | alt | 195 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -21.1) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0811× (z -16.7) |
| [[RPMI-7951 (line)]] | alt | 102 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0355× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.110× (z -14.6) |
| [[HepG2_C3A (line)]] | wt | 115 | 0 | 7 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0233× (z -22.3) ⚠ toxic; cell-cycle shift, explains ~33% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.0953× (z -14.5) |
| [[HS-578T (line)]] | alt | 78.3 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0572× (z -12.5) |
| [[HT-29 (line)]] | alt | 23.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0698× (z -16.3) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.182× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 70.5 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0701× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0743× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 35.2 | 0 | 5 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0443× (z -14.5) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1792 (line)]] | alt | 18.0 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0550× (z -13.5) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -9.7) |
| [[A-172 (line)]] | wt | 16.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +19.3) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 12.6× (z +13.2) | — |
| [[A549 (line)]] | wt | 26.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -11.9) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.102× (z -8.8) |
| [[HOP62 (line)]] | alt | 24.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 21.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -9.8) ⚠ cell-cycle shift, explains ~68% of this change |
| [[CFPAC-1 (line)]] | alt | 17.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.107× (z -9.5) |
| [[CHP-212 (line)]] | wt | 46.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0302× (z -11.3) ⚠ cell-cycle shift, explains ~42% of this change |
| [[H4 (line)]] | wt | 47.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.111× (z -10.6) |
| [[Hs 766T (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -9.8) ⚠ cell-cycle shift, explains ~68% of this change |
| [[NCI-H1573 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.175× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 10.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +10.0) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[A-427 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.00 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.81 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.26 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13806), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMP3]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[MIR3681HG]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[SYN3]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[MDGA2]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[SETBP1]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[IGFBP5]] | +0.61 | +0.58 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[LINC00298]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[PTPRD]] | +0.57 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[AIM2]] | +0.57 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[SORCS1]] | +0.57 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[EPHA3]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[ALK]] | +0.56 | +0.49 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 18, C 4. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARMN]] | B | CARMN activity raises DIRC3's level | lines that do not express CARMN (40) vs lines expressing it (10) | 5.70× lower at baseline in the lines without CARMN | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN |
| [[CTTNBP2]] | B | CTTNBP2 activity raises DIRC3's level | lines that do not express CTTNBP2 (31) vs lines expressing it (19) | 2.58× lower at baseline in the lines without CTTNBP2 | 0.011 | ⚠ within organs, on part of the lines; also absent: DCT, ENSG00000266976, TYR |
| [[AEBP1]] | B | AEBP1 activity raises DIRC3's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 5.14× lower at baseline in the lines without AEBP1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1 |
| [[FKBP9P1-1]] | B | FKBP9P1-1 activity raises DIRC3's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 2.98× lower at baseline in the lines without FKBP9P1-1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[ITIH5]] | B | ITIH5 activity raises DIRC3's level | lines that do not express ITIH5 (37) vs lines expressing it (13) | 4.31× lower at baseline in the lines without ITIH5 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GDNF, TDRD9, ENSG00000234426 |
| [[PLOD2]] | B | PLOD2 activity raises DIRC3's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 3.73× lower at baseline in the lines without PLOD2 | 0.018 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[CFI]] | B | CFI activity raises DIRC3's level | lines that do not express CFI (31) vs lines expressing it (19) | 2.70× lower at baseline in the lines without CFI | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1 |
| [[TIMP3]] | B | TIMP3 activity raises DIRC3's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 3.52× lower at baseline in the lines without TIMP3 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1 |
| [[LINC01287]] | B | LINC01287 activity raises DIRC3's level | lines that do not express LINC01287 (39) vs lines expressing it (11) | 3.85× lower at baseline in the lines without LINC01287 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253642, POU6F2, RIT2 |
| [[FCRLA]] | B | FCRLA activity raises DIRC3's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 5.00× lower at baseline in the lines without FCRLA | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474 |
| [[IGFBP5]] | B | IGFBP5 activity raises DIRC3's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 3.32× lower at baseline in the lines without IGFBP5 | 0.052 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2 |
| [[AK4P3]] | B | AK4P3 activity raises DIRC3's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.79× lower at baseline in the lines without AK4P3 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 16, C 8. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTCP1]] | B | DIRC3 activity raises MTCP1's level | lines that do not express DIRC3 (19) vs lines expressing it (31) | 1.53× lower at baseline in the lines without DIRC3 | 0.007 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |
| [[UBA6-DT]] | B | DIRC3 activity raises UBA6-DT's level | lines that do not express DIRC3 (19) vs lines expressing it (31) | 2.14× lower at baseline in the lines without DIRC3 | 0.024 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |
| [[LINC00298]] | B | DIRC3 activity raises LINC00298's level | lines that do not express DIRC3 (19) vs lines expressing it (31) | 2.03× lower at baseline in the lines without DIRC3 | 0.045 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |
| [[SYN3]] | B | DIRC3 activity raises SYN3's level | lines that do not express DIRC3 (19) vs lines expressing it (31) | 2.07× lower at baseline in the lines without DIRC3 | 0.047 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |
| [[EGLN3]] | B | DIRC3 activity raises EGLN3's level | lines that do not express DIRC3 (19) vs lines expressing it (31) | 1.52× lower at baseline in the lines without DIRC3 | 0.052 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |
| [[SMIM2-AS1]] | B | DIRC3 activity raises SMIM2-AS1's level | lines that do not express DIRC3 (19) vs lines expressing it (31) | 1.90× lower at baseline in the lines without DIRC3 | 0.054 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |
| [[MTCP1]] | B | DIRC3 activity strengthens MTCP1's drug response | lines that do not express DIRC3 (19) vs lines expressing it (29) | the lines without DIRC3 respond 1.02× as strongly (z diff -0.02); rises at some drug-doses, falls at others (74% from rises): Cobimetinib 5 µM: 1.15x vs 2.01x (z diff +2.0); Digitoxin 0.5 µM: 0.68x vs 0.52x (z diff +1.5); Harringtonine 5 µM: 0.77x vs 0.53x (z diff +1.4) | 0.066 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |
| [[NDNF]] | B | DIRC3 activity raises NDNF's level | lines that do not express DIRC3 (19) vs lines expressing it (31) | 1.97× lower at baseline in the lines without DIRC3 | 0.071 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |
| [[LINC03047]] | B | DIRC3 activity raises LINC03047's level | lines that do not express DIRC3 (19) vs lines expressing it (31) | 3.02× lower at baseline in the lines without DIRC3 | 0.071 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |
| [[ENOX1]] | B | DIRC3 activity raises ENOX1's level | lines that do not express DIRC3 (19) vs lines expressing it (31) | 1.69× lower at baseline in the lines without DIRC3 | 0.081 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |
| [[SLC14A2]] | B | DIRC3 activity raises SLC14A2's level | lines that do not express DIRC3 (19) vs lines expressing it (31) | 1.76× lower at baseline in the lines without DIRC3 | 0.081 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |
| [[LINC00276]] | B | DIRC3 activity raises LINC00276's level | lines that do not express DIRC3 (19) vs lines expressing it (31) | 1.53× lower at baseline in the lines without DIRC3 | 0.094 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.335). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (50.7, 27.1); signed map (29.9, 41.6). **Vector** length 84.2, 21.4% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +10.1 | -0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +9.7 | +2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +8.5 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.1 | +8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | -1.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.7 | +0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +2.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.0 | -5.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.0 | -3.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.8 | +0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.7 | +0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -3.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -0.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.3 | -1.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.2 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | disrupted in renal carcinoma 3 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q35 — chr2:217,284,019-217,756,593 (-) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ14199 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:17805](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17805) · Entrez [729582](https://www.ncbi.nlm.nih.gov/gene/729582) · Ensembl [ENSG00000231672](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231672)

## Data

Gene col 13806: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13806); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13806, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13806]; `tensor/DDL_lfc|DDL_z.npy` [13806]; `embed/gene_vectors.npy` [13806]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13806 or target_col == 13806). Every well: [[DIRC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIRC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
