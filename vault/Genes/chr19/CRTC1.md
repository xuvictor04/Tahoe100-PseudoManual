---
symbol: "CRTC1"
type: "gene"
col: 2640
ensembl_id: "ENSG00000105662"
name: "CREB regulated transcription coactivator 1"
location: "19p13.11"
module: 3
arm: "+"
pooled_cpm: 45.81
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 35
n_dd_up_clean: 0
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CRTC1

*CREB regulated transcription coactivator 1* — 19p13.11

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 2.20×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.455× (z -24.4, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL26]] (+0.66, fdr 1e-05, ⚠ same locus), [[VPS37C]] (+0.64, fdr 1e-05), [[FAM13B]] (+0.64, fdr 1e-05), [[RBM4B]] (+0.63, fdr 7e-06); moves opposite to [[STX16]] (-0.56, fdr 4e-05), [[STMP1]] (-0.56, fdr 3e-05), [[AP5M1]] (-0.55, fdr 3e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2640.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 2.20×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.16× | +3.3 | 0.31 | 7/48 (HCT15, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.3 | 0.31 | 17/48 (Hs 766T, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 21 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2640.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.455×** | -24.4 | 0e+00 | 44/48 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.397×** | -19.4 | 0e+00 | 33/40 (LoVo, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.416×** | -19.2 | 0e+00 | 41/48 (HCT15, Panc 03.27, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.389×** | -19.1 | 0e+00 | 38/45 (SHP-77, H4, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.435×** | -17.5 | 0e+00 | 43/48 (SNU-423, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.464×** | -16.1 | 0e+00 | 43/48 (NCI-H2347, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.558×** | -12.7 | 3e-35 | 43/48 (RPMI-7951, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.599×** | -10.7 | 5e-25 | 34/47 (H4, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.636×** | -9.9 | 3e-21 | 41/48 (NCI-H661, LoVo, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.722×** | -7.1 | 8e-11 | 28/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.723×** | -7.1 | 8e-11 | 25/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.726×** | -7.0 | 1e-10 | 29/48 (SW 900, HS-578T, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.728×** | -6.9 | 2e-10 | 32/48 (MIA PaCa-2, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.546×** | -6.9 | 2e-10 | 33/49 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.739×** | -6.6 | 2e-09 | 30/48 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.807×** | -6.6 | 2e-09 | 25/48 (HOP62, SNU-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.590×** | -6.0 | 6e-08 | 27/48 (HS-578T, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.814×** | -4.5 | 2e-04 | 19/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.809×** | -4.4 | 2e-04 | 21/47 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.810×** | -4.3 | 3e-04 | 21/48 (SW 900, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.829×** | -4.1 | 9e-04 | 18/48 (SW 900, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2640. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 61.5 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -15.2) |
| [[C-33 A (line)]] | alt | 84.2 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -13.2) |
| [[NCI-H2347 (line)]] | alt | 50.7 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -18.3) |
| [[RPMI-7951 (line)]] | alt | 65.5 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -18.3) |
| [[HEC-1-A (line)]] | alt | 87.4 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -10.7) |
| [[HOP62 (line)]] | alt | 35.7 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -15.2) |
| [[HS-578T (line)]] | alt | 56.0 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -14.1) |
| [[NCI-H460 (line)]] | wt | 41.7 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 70.7 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -10.7) |
| [[PANC-1 (line)]] | alt | 32.0 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -14.7) |
| [[SW480 (line)]] | alt | 57.1 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -19.8) |
| [[LoVo (line)]] | wt | 42.0 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0988× (z -23.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -9.7) |
| [[LS 180 (line)]] | wt | 50.2 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -13.0) |
| [[RKO (line)]] | wt | 57.4 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.109× (z -20.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -11.1) |
| [[SNU-423 (line)]] | alt | 52.5 | 0 | 5 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0974× (z -21.0) |
| [[CFPAC-1 (line)]] | alt | 40.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 35.8 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 50.1 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -17.7) |
| [[SK-MEL-2 (line)]] | alt | 37.6 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -12.7) |
| [[A-172 (line)]] | wt | 41.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | [[Lonafarnib (drug)]] 5 µM 0.152× (z -9.0) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -8.7) |
| [[H4 (line)]] | wt | 67.0 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0516× (z -21.2) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 46.7 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -13.2) |
| [[NCI-H2030 (line)]] | alt | 51.7 | 0 | 3 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -11.1) |
| [[SW 900 (line)]] | alt | 45.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -9.2) |
| [[SW48 (line)]] | wt | 77.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 28.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -14.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 35.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[COLO 205 (line)]] | alt | 57.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -9.4) |
| [[HCT15 (line)]] | alt | 91.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0518× (z -26.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[Hs 766T (line)]] | wt | 26.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -10.7) |
| [[J82 (line)]] | alt | 31.1 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -11.0) |
| [[SW1417 (line)]] | alt | 48.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -13.1) |
| [[A-427 (line)]] | wt | 45.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -9.1) |
| [[AN3 CA (line)]] | alt | 50.3 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0497× (z -14.1) |
| [[C32 (line)]] | wt | 40.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -9.8) |
| [[CHP-212 (line)]] | wt | 82.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 46.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -11.1) |
| [[HT-29 (line)]] | alt | 33.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -10.0) |
| [[NCI-H661 (line)]] | alt | 41.9 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0858× (z -8.6) |
| [[SHP-77 (line)]] | alt | 42.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0914× (z -19.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 65.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -12.2) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 69.4 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.100× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2640), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL26]] | +0.66 | +0.62 / +0.51 | both halves | 1e-05 | ⚠ same locus (12.0 kb, same strand: neighbours can correlate without regulation) |
| [[VPS37C]] | +0.64 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[FAM13B]] | +0.64 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[RBM4B]] | +0.63 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[DDX19B]] | +0.63 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[TTC38]] | +0.61 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[SUFU]] | +0.61 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[BTBD2]] | +0.60 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[RANBP10]] | +0.59 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[LAGE3]] | +0.59 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[MAP2K7]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[CNNM4]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[AFMID]] | +0.58 | +0.58 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX16]] | -0.56 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[STMP1]] | -0.56 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[AP5M1]] | -0.55 | -0.52 / -0.27 | both halves | 3e-04 |  |
| [[TOR1A]] | -0.54 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[SETD7]] | -0.53 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[EIF4G2]] | -0.53 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[MSL3]] | -0.53 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[SAP30L-AS1]] | -0.52 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[MOB1A]] | -0.51 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[TUG1]] | -0.51 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[TWF1]] | -0.51 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[RNF217-AS1]] | -0.50 | -0.22 / -0.50 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CRTC1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.422). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-34.2, -12.3); signed map (-32.9, 0.6). **Vector** length 103, 27.4% of its response variance represented; |z| ≥ 3 in 1,172 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.5 | +3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.3 | +2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +4.2 | -3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +3.9 | +0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +2.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.7 | +1.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.5 | +1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +2.7 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -17.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -8.4 | -16.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.1 | -24.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.5 | -12.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -6.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | CREB regulated transcription coactivator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,683,678-18,782,333 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0616, FLJ14027, TORC1; previously MECT1 |
| Reactome | 9 pathways, smallest: Phosphorylated BMAL1:CLOCK (ARNTL:CLOCK) activates expression of core clock genes; Expression of BMAL (ARNTL), CLOCK, and NPAS2; Heme signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UUV9](https://www.uniprot.org/uniprotkb/Q6UUV9) (CREB-regulated transcription coactivator 1):

> Transcriptional coactivator for CREB1 which activates transcription through both consensus and variant cAMP response element (CRE) sites. Acts as a coactivator, in the SIK/TORC signaling pathway, being active when dephosphorylated and acts independently of CREB1 'Ser-133' phosphorylation. Enhances the interaction of CREB1 with TAF4. Regulates the expression of specific CREB-activated genes such as the steroidogenic gene, StAR. Potent coactivator of PGC1alpha and inducer of mitochondrial …

**Summary**, from NCBI Gene [23373](https://www.ncbi.nlm.nih.gov/gene/23373):

> Enables cAMP response element binding protein binding activity. Involved in positive regulation of transcription by RNA polymerase II. Located in cytosol and nuclear body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16062](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16062) · Entrez [23373](https://www.ncbi.nlm.nih.gov/gene/23373) · UniProt [Q6UUV9](https://www.uniprot.org/uniprotkb/Q6UUV9) · Ensembl [ENSG00000105662](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105662)

## Data

Gene col 2640: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2640); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2640, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2640]; `tensor/DDL_lfc|DDL_z.npy` [2640]; `embed/gene_vectors.npy` [2640]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2640 or target_col == 2640). Every well: [[CRTC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRTC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
