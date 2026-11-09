---
symbol: "GTSE1"
type: "gene"
col: 1105
ensembl_id: "ENSG00000075218"
name: "G2 and S-phase expressed 1"
location: "22q13.31"
module: 22
arm: "+"
pooled_cpm: 38.94
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 16
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# GTSE1

*G2 and S-phase expressed 1* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.71× (z +6.0, q 1e-06, up in 34 of 45 measured lines) ⚠ transcription drop; cell-cycle shift, would explain all of this change. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 1.50× (z +4.3, q 0.002, up in 29 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (12 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.450× (z -12.4, q 8e-33, down in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~68% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.636× (z -5.0, q 8e-05, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDCA8]] (+0.95, fdr 7e-06), [[TACC3]] (+0.94, fdr 7e-06), [[KIF2C]] (+0.94, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1105.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.71×** | +6.0 | 1e-06 | 34/45 (SW 900, HT-29, …) | all doses, flat | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.43×** | +5.7 | 4e-06 | 35/47 (NCI-H23, SW 900, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.58×** | +5.1 | 8e-05 | 25/44 (Panc 03.27, SNU-1, …) | two highest doses | composition shift; position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.14×** | +4.4 | 0.001 | 26/45 (NCI-H23, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.50×** | +4.3 | 0.002 | 29/46 (HOP62, A549, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.51×** | +4.2 | 0.002 | 24/47 (SW 900, KATO III, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.46×** | +4.2 | 0.002 | 27/46 (HOP62, H4, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.44×** | +3.9 | 0.006 | 21/38 (Panc 03.27, A-172, …) | two highest doses | composition shift; position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.42×** | +3.9 | 0.006 | 24/46 (HOP62, SW 900, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.41×** | +3.9 | 0.006 | 24/47 (HT-29, HOP62, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.40×** | +3.7 | 0.011 | 19/47 (HT-29, SW 900, …) | two highest doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.39×** | +3.7 | 0.011 | 22/47 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.012 | 19/47 (HT-29, HEC-1-A, …) | all doses, flat |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.36×** | +3.4 | 0.026 | 19/47 (SW 900, Panc 03.27, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.35×** | +3.4 | 0.027 | 17/47 (NCI-H2030, HT-29, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.61×** | +3.3 | 0.035 | 18/47 (HOP62, HEC-1-A, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.066 | 11/47 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **1.69×** | +3.0 | 0.074 | 15/44 (HOP62, SW 900, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1105.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.450×** | -12.4 | 8e-33 | 43/47 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.367×** | -11.0 | 7e-26 | 45/47 (LS 180, H4, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.423×** | -7.7 | 3e-12 | 34/47 (KATO III, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.570×** | -6.2 | 9e-08 | 35/46 (HEC-1-A, NCI-H1573, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.636×** | -5.0 | 8e-05 | 32/47 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.639×** | -4.9 | 9e-05 | 36/47 (Hs 766T, A549, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~64% of this change | **0.445×** | -4.7 | 3e-04 | 28/42 (SHP-77, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.650×** | -4.6 | 4e-04 | 27/47 (NCI-H1573, SNU-1, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.670×** | -4.4 | 7e-04 | 26/46 (NCI-H1573, SNU-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.688×** | -4.1 | 0.002 | 23/47 (RPMI-7951, H4, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.703×** | -3.9 | 0.006 | 23/47 (H4, A-172, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.570×** | -3.8 | 0.006 | 26/47 (SW480, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.799×** | -3.5 | 0.023 | 21/47 (HT-29, HCT15, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.820×** | -3.1 | 0.084 | 21/47 (H4, Hs 766T, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.757×** | -3.0 | 0.084 | 16/47 (NCI-H2030, KATO III, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.758×** | -3.0 | 0.084 | 21/47 (HEC-1-A, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +1.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1105. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 63.7 | 0 | 7 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.100× (z -16.8) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.230× (z -10.7) |
| [[A498 (line)]] | wt | 37.9 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.153× (z -17.5) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.385× (z -8.9) |
| [[A549 (line)]] | wt | 26.7 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.193× (z -14.5) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.159× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 27.5 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.130× (z -15.1) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.163× (z -9.5) |
| [[A-172 (line)]] | wt | 39.3 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.160× (z -12.3) ⚠ cell-cycle shift, explains ~62% of this change |
| [[LS 180 (line)]] | wt | 33.3 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.121× (z -13.6) ⚠ cell-cycle shift, explains ~68% of this change |
| [[NCI-H1573 (line)]] | alt | 26.7 | 0 | 3 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.159× (z -10.1) ⚠ cell-cycle shift, explains ~60% of this change |
| [[SNU-1 (line)]] | wt | 45.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0470× (z -13.2) |
| [[A-427 (line)]] | wt | 54.4 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.127× (z -19.7) ⚠ cell-cycle shift, explains ~68% of this change |
| [[C32 (line)]] | wt | 60.6 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.219× (z -13.0) ⚠ cell-cycle shift, explains ~68% of this change |
| [[HEC-1-A (line)]] | alt | 62.6 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.264× (z -10.4) |
| [[HT-29 (line)]] | alt | 25.3 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.175× (z -9.9) ⚠ cell-cycle shift, explains ~62% of this change |
| [[NCI-H460 (line)]] | wt | 25.2 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.332× (z -11.0) ⚠ cell-cycle shift, explains ~68% of this change |
| [[AN3 CA (line)]] | alt | 86.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.114× (z -10.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 78.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.309× (z -9.0) ⚠ cell-cycle shift, explains ~68% of this change |
| [[HOP62 (line)]] | alt | 72.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.335× (z -11.5) ⚠ cell-cycle shift, explains ~68% of this change |
| [[Hs 766T (line)]] | wt | 35.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.153× (z -14.8) ⚠ cell-cycle shift, explains ~68% of this change |
| [[HS-578T (line)]] | alt | 51.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.399× (z -9.2) ⚠ cell-cycle shift, explains ~68% of this change |
| [[hTERT-HPNE (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.179× (z -10.9) ⚠ cell-cycle shift, explains ~68% of this change |
| [[LoVo (line)]] | wt | 29.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.402× (z -8.5) ⚠ cell-cycle shift, explains ~68% of this change |
| [[MIA PaCa-2 (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 57.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 28.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.187× (z -13.7) ⚠ cell-cycle shift, explains ~68% of this change |
| [[SHP-77 (line)]] | alt | 78.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 6.67 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 41.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1105), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDCA8]] | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 643 |
| [[TACC3]] | +0.94 | +0.93 / +0.94 | both halves | 7e-06 | STRING 594 |
| [[KIF2C]] | +0.94 | +0.92 / +0.93 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 754 |
| [[KIF18B]] | +0.92 | +0.89 / +0.93 | both halves | 7e-06 | STRING 625 |
| [[NDC80]] | +0.90 | +0.90 / +0.90 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 511 |
| [[HJURP]] | +0.90 | +0.87 / +0.91 | both halves | 7e-06 | pathway: G2/M Transition; STRING 889 |
| [[KNL1]] | +0.90 | +0.91 / +0.87 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 516 |
| [[KIF23]] | +0.90 | +0.91 / +0.87 | both halves | 7e-06 | STRING 624 |
| [[SGO2]] | +0.89 | +0.89 / +0.89 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[MKI67]] | +0.89 | +0.91 / +0.87 | both halves | 7e-06 | STRING 834 |
| [[KIF4A]] | +0.89 | +0.94 / +0.84 | both halves | 7e-06 | STRING 664 |
| [[DLGAP5]] | +0.88 | +0.89 / +0.86 | both halves | 7e-06 | STRING 736 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 2, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises GTSE1's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.38× lower at baseline in the lines without PIMREG | 0.006 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises GTSE1's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.11× lower at baseline in the lines without NEURL1B | 0.054 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[NDC80]] | C | NDC80 activity raises GTSE1's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.78× lower at baseline in the lines without NDC80 | 0.026 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[PBK]] | C | PBK activity raises GTSE1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.71× lower at baseline in the lines without PBK | 0.037 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises GTSE1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.51× lower at baseline in the lines without AURKB | 0.039 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[MYLK2]] | C | MYLK2 activity raises GTSE1's level | lines that do not express MYLK2 (3) vs lines expressing it (47) | 3.17× lower at baseline in the lines without MYLK2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, NDC80, SMARCD3; maybe low, not absent; its own permutation p |
| [[FAM72D]] | C | FAM72D activity raises GTSE1's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.86× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises GTSE1's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.33× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[C21orf58]] | C | C21orf58 activity raises GTSE1's level | lines that do not express C21orf58 (3) vs lines expressing it (47) | 3.01× lower at baseline in the lines without C21orf58 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p |
| [[CDC20]] | C | CDC20 activity raises GTSE1's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.44× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[TP53]] | C | TP53 activity strengthens GTSE1's drug response | recorded loss-of-function mutation of TP53 in 30 lines vs 17 not recorded | the TP53-altered lines respond 0.91× as strongly (z diff +0.19); strongest at Selinexor 5 µM: 0.51x vs 0.24x (z diff +2.6) | 0.728 over the table, 0.047 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.926). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.5, -56.1); signed map (-49.8, -42.2). **Vector** length 150, 55.6% of its response variance represented; |z| ≥ 3 in 1,142 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.74 to 60); *DREAM G2/M down* (control, mean cos +0.83 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.70 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +5.5 | +5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.1 | -1.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +4.8 | +6.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.4 | +1.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +1.2 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +3.3 | +3.7 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.1 | +3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +2.9 | +3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.9 | +4.3 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | +2.8 | +4.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -9.7 | -12.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -9.5 | -11.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | -6.2 | -7.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -5.7 | -6.2 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~77% of this change | -5.7 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -3.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.8 | -2.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.9 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | G2 and S-phase expressed 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:46,296,870-46,330,810 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GTSE-1, B99, Lnc_bc060912 |
| Reactome | 7 pathways, smallest: The role of GTSE1 in G2/M progression after G2 checkpoint; G2/M Checkpoints; G2/M Transition |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYZ3](https://www.uniprot.org/uniprotkb/Q9NYZ3) (G2 and S phase-expressed protein 1):

> May be involved in p53-induced cell cycle arrest in G2/M phase by interfering with microtubule rearrangements that are required to enter mitosis. Overexpression delays G2/M phase progression.

**Summary**, from NCBI Gene [51512](https://www.ncbi.nlm.nih.gov/gene/51512):

> The protein encoded by this gene is only expressed in the S and G2 phases of the cell cycle, where it colocalizes with cytoplasmic tubulin and microtubules. In response to DNA damage, the encoded protein accumulates in the nucleus and binds the tumor suppressor protein p53, shuttling it out of the nucleus and repressing its ability to induce apoptosis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13698](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13698) · Entrez [51512](https://www.ncbi.nlm.nih.gov/gene/51512) · UniProt [Q9NYZ3](https://www.uniprot.org/uniprotkb/Q9NYZ3) · Ensembl [ENSG00000075218](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075218)

## Data

Gene col 1105: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1105); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1105, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1105]; `tensor/DDL_lfc|DDL_z.npy` [1105]; `embed/gene_vectors.npy` [1105]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1105 or target_col == 1105). Every well: [[GTSE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTSE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
