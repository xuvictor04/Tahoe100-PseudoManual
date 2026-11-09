---
symbol: "SHPK"
type: "gene"
col: 12396
ensembl_id: "ENSG00000197417"
name: "sedoheptulokinase"
location: "17p13.2"
module: 52
arm: "+"
pooled_cpm: 22.83
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 16
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# SHPK

*sedoheptulokinase* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.51× (z +23.6, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.590× (z -9.6, q 3e-19, down in 27 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.644× (z -8.1, q 1e-13, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRPV1]] (+0.81, fdr 7e-06, ⚠ same locus), [[POLG]] (+0.63, fdr 1e-05), [[FBH1]] (+0.61, fdr 1e-04), [[RABGEF1]] (+0.61, fdr 2e-05); moves opposite to [[LYPLAL1]] (-0.59, fdr 1e-05), [[CHIC1]] (-0.54, fdr 1e-04), [[RPS6KA6]] (-0.53, fdr 2e-04).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12396.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.51×** | +23.6 | 0e+00 | 43/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.26×** | +14.8 | 0e+00 | 42/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.19×** | +14.3 | 5e-44 | 40/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.91×** | +11.8 | 1e-29 | 38/48 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +11.2 | 7e-27 | 37/47 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.61×** | +8.6 | 6e-16 | 30/47 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +7.4 | 1e-11 | 28/48 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +6.6 | 3e-09 | 21/48 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.32×** | +5.1 | 2e-05 | 17/47 (PANC-1, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.6 | 2e-04 | 24/47 (LS 180, HOP62, …) | top dose only | composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.62×** | +4.6 | 2e-04 | 13/46 (SW480, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.25×** | +4.0 | 0.003 | 16/48 (A498, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.7 | 0.009 | 1/48 (NCI-H1792) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.21×** | +3.4 | 0.026 | 13/47 (C-33 A, SW1417, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.090 | 10/48 (NCI-H2030, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12396.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.590×** | -9.6 | 3e-19 | 27/39 (A-172, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.588×** | -9.4 | 2e-18 | 30/47 (NCI-H2347, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.639×** | -8.2 | 4e-14 | 29/46 (SW 900, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.644×** | -8.1 | 1e-13 | 31/48 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.690×** | -6.8 | 1e-09 | 26/48 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.690×** | -6.5 | 6e-09 | 19/32 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.659×** | -6.5 | 8e-09 | 25/36 (SNU-423, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.736×** | -5.4 | 5e-06 | 25/46 (SNU-423, COLO 205, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.753×** | -5.2 | 1e-05 | 22/47 (PANC-1, BT-474, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.773×** | -4.7 | 1e-04 | 24/48 (HS-578T, SW 900, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.714×** | -4.3 | 8e-04 | 14/48 (H4, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -4.0 | 0.003 | 16/48 (KATO III, HT-29, …) | top dose only | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.662×** | -4.0 | 0.003 | 13/40 (HepG2/C3A, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.868× | -3.7 | 0.009 | 16/48 (NCI-H1792, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.819×** | -3.7 | 0.009 | 14/48 (H4, SW480, …) | all doses, stronger at high dose |  |
| [[Regorafenib (drug)]] 5 µM |  | **0.715×** | -3.2 | 0.043 | 6/46 (SNU-1, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **0.769×** | -3.0 | 0.090 | 6/48 (COLO 205, BT-474, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12396. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 27.2 | 6 | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.10× (z +15.5) | [[Harringtonine (drug)]] 0.5 µM 0.376× (z -8.9) |
| [[A549 (line)]] | wt | 34.9 | 3 | 3 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.79× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.208× (z -10.2) |
| [[SW480 (line)]] | alt | 33.8 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.208× (z -15.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 41.3 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -12.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 23.3 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -10.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 25.7 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.50× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.263× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 17.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +19.0) | — |
| [[LoVo (line)]] | wt | 22.4 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +14.8) | — |
| [[NCI-H2030 (line)]] | alt | 22.6 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 26.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -15.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 18.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.159× (z -10.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 30.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +12.4) | [[Lonafarnib (drug)]] 5 µM 0.129× (z -9.4) ⚠ toxic |
| [[KATO III (line)]] | alt | 28.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.156× (z -12.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 14.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +13.7) | — |
| [[NCI-H1792 (line)]] | alt | 17.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.68× (z +13.2) | — |
| [[NCI-H23 (line)]] | alt | 25.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +8.7) | [[Harringtonine (drug)]] 5 µM 0.295× (z -8.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H2347 (line)]] | alt | 16.4 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.190× (z -11.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 13.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +12.4) | — |
| [[SNU-423 (line)]] | alt | 19.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0685× (z -15.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 19.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -11.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 17.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.60× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 24.4 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0656× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -11.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.183× (z -10.2) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 21.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 13.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 18.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 16.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +10.7) | — |
| [[RKO (line)]] | wt | 18.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 18.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +9.4) | — |
| [[SW48 (line)]] | wt | 27.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -10.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12396), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRPV1]] | +0.81 | +0.75 / +0.86 | both halves | 7e-06 | STRING 549; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[POLG]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[FBH1]] | +0.61 | +0.35 / +0.69 | both halves | 1e-04 |  |
| [[RABGEF1]] | +0.61 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[PRPSAP1]] | +0.60 | +0.46 / +0.69 | both halves | 3e-05 |  |
| [[SLC10A3]] | +0.59 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[GLE1]] | +0.58 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[SENP5]] | +0.57 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[ZFYVE21]] | +0.57 | +0.36 / +0.60 | both halves | 1e-04 |  |
| [[TTLL3]] | +0.57 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[NDEL1]] | +0.55 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[IL9RP3]] | +0.54 | +0.37 / +0.57 | both halves | 9e-05 |  |
| [[DEPDC5]] | +0.53 | +0.36 / +0.57 | both halves | 9e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYPLAL1]] | -0.59 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[CHIC1]] | -0.54 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[RPS6KA6]] | -0.53 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[PTAR1]] | -0.53 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[SPTLC3]] | -0.53 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[MRPL47]] | -0.52 | -0.09 / -0.69 | ⚠ one half (not replicated) | 0.003 |  |
| [[TMEM218]] | -0.52 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[NUDT9]] | -0.52 | -0.24 / -0.63 | both halves | 4e-04 |  |
| [[IRAK1BP1]] | -0.51 | -0.43 / -0.49 | both halves | 4e-05 |  |
| [[N6AMT1]] | -0.51 | -0.25 / -0.56 | both halves | 4e-04 |  |
| [[IFTAP]] | -0.50 | -0.26 / -0.58 | both halves | 4e-04 |  |
| [[PPA2]] | -0.50 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[NBEA]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SHPK's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers SHPK's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers SHPK's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.487). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (19.0, -16.3); signed map (-21.7, 41.7). **Vector** length 80.3, 15.7% of its response variance represented; |z| ≥ 3 in 1,085 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +23.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +11.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.3 | +8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +6.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.8 | +4.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +1.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.5 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -6.1 | -9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.5 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -5.4 | -3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -8.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.3 | -5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | sedoheptulokinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:3,608,240-3,636,250 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SHK; previously CARKL |
| Gene groups (HGNC) | Carbohydrate kinases; FGGY kinase family |
| Reactome | 2 pathways, smallest: Pentose phosphate pathway; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHJ6](https://www.uniprot.org/uniprotkb/Q9UHJ6) (Sedoheptulokinase):

> Acts as a modulator of macrophage activation through control of glucose metabolism.

**Summary**, from NCBI Gene [23729](https://www.ncbi.nlm.nih.gov/gene/23729):

> The protein encoded by this gene has weak homology to several carbohydrate kinases, a class of proteins involved in the phosphorylation of sugars as they enter a cell, inhibiting return across the cell membrane. Sequence variation between this novel gene and known carbohydrate kinases suggests the possibility of a different substrate, cofactor or changes in kinetic properties distinguishing it from other carbohydrate kinases. The gene resides in a region commonly deleted in cystinosis patients, …

**Accessions** — [HGNC:1492](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1492) · Entrez [23729](https://www.ncbi.nlm.nih.gov/gene/23729) · UniProt [Q9UHJ6](https://www.uniprot.org/uniprotkb/Q9UHJ6) · Ensembl [ENSG00000197417](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197417)

## Data

Gene col 12396: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12396); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12396, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12396]; `tensor/DDL_lfc|DDL_z.npy` [12396]; `embed/gene_vectors.npy` [12396]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12396 or target_col == 12396). Every well: [[SHPK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHPK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
