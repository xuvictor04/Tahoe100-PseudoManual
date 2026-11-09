---
symbol: "AOPEP"
type: "gene"
col: 7243
ensembl_id: "ENSG00000148120"
name: "aminopeptidase O (putative)"
location: "9q22.32"
module: 66
arm: "+"
pooled_cpm: 240.43
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 32
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# AOPEP

*aminopeptidase O (putative)* — 9q22.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.39× (z +4.5, q 0.004, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (20 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.496× (z -9.5, q 2e-18, down in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.581× (z -7.6, q 3e-12, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP42]] (+0.55, fdr 2e-05), [[AKR1C3]] (+0.52, fdr 1e-04), [[MID1]] (+0.52, fdr 4e-05); moves opposite to [[PPP2R2C]] (-0.50, fdr 3e-05), [[CAPRIN2]] (-0.49, fdr 2e-05), [[ZNF699]] (-0.47, fdr 4e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SOX6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7243.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +4.5 | 0.004 | 36/47 (A549, HOP62, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.74×** | +4.1 | 0.012 | 35/50 (AsPC-1, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +4.0 | 0.012 | 28/48 (AsPC-1, A549, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.37×** | +3.9 | 0.014 | 35/50 (AsPC-1, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.12 | 21/49 (AsPC-1, NCI-H460, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.31× | +3.2 | 0.14 | 27/47 (AsPC-1, A549, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7243.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.496×** | -9.5 | 2e-18 | 44/48 (NCI-H1792, A549, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.526×** | -8.7 | 9e-16 | 39/44 (SK-MEL-2, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.540×** | -8.7 | 9e-16 | 45/48 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.581×** | -7.6 | 3e-12 | 41/48 (SW480, SW 900, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.604×** | -7.1 | 2e-10 | 42/48 (NCI-H460, KATO III, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.701×** | -7.0 | 2e-10 | 32/49 (A549, CHP-212, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.636×** | -6.1 | 8e-08 | 39/47 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.631×** | -6.0 | 2e-07 | 34/45 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **0.657×** | -5.9 | 2e-07 | 42/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.603×** | -5.9 | 2e-07 | 36/49 (LoVo, C-33 A, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.672×** | -5.6 | 1e-06 | 38/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.621×** | -5.6 | 1e-06 | 38/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.762×** | -5.4 | 3e-06 | 27/48 (NCI-H1792, SW 900, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.698×** | -4.9 | 5e-05 | 34/50 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.722×** | -4.6 | 2e-04 | 31/48 (A549, SW 900, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.797×** | -4.5 | 2e-04 | 27/49 (SW 900, NCI-H1792, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.736×** | -4.1 | 0.002 | 32/48 (SW 900, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.747×** | -3.9 | 0.003 | 30/48 (AsPC-1, SW 900, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.767×** | -3.7 | 0.005 | 28/48 (SW 900, CFPAC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.714×** | -3.4 | 0.016 | 29/48 (SW 900, KATO III, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.787×** | -3.4 | 0.017 | 24/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.788×** | -3.2 | 0.027 | 26/47 (SW 900, NCI-H1792, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.781×** | -2.9 | 0.074 | 25/47 (SW 900, AsPC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7243. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 339 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -17.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.266× (z -12.7) |
| [[LoVo (line)]] | wt | 368 | 0 | 10 (9 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.266× (z -13.7) ⚠ toxic; cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.451× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 297 | 0 | 10 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.206× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.255× (z -10.4) |
| [[A549 (line)]] | wt | 341 | 3 (1 ⚠) | 6 (3 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.82× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -17.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -13.4) |
| [[MIA PaCa-2 (line)]] | alt | 166 | 0 | 7 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.305× (z -13.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.396× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 389 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -20.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -9.8) |
| [[SHP-77 (line)]] | alt | 335 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -12.5) |
| [[KATO III (line)]] | alt | 414 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.324× (z -13.0) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.425× (z -9.9) |
| [[PANC-1 (line)]] | alt | 233 | 0 | 6 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.312× (z -13.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[AsPC-1 (line)]] | alt | 120 | 5 (1 ⚠) | 0 | [[Trametinib (drug)]] 5 µM 3.11× (z +11.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Trametinib (drug)]] 0.05 µM 2.26× (z +11.0) | — |
| [[A-172 (line)]] | wt | 217 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +13.8) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.327× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[CFPAC-1 (line)]] | alt | 158 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -14.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 178 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -16.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.431× (z -9.0) |
| [[HOP62 (line)]] | alt | 158 | 1 | 3 (3 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.30× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.422× (z -9.5) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H23 (line)]] | alt | 213 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SW1417 (line)]] | alt | 217 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -12.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 428 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.251× (z -13.7) |
| [[A498 (line)]] | wt | 241 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -12.4) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 489 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -13.1) |
| [[NCI-H2347 (line)]] | alt | 201 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.282× (z -13.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 171 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0800× (z -23.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A-427 (line)]] | wt | 136 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.366× (z -12.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[AN3 CA (line)]] | alt | 350 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[C-33 A (line)]] | alt | 250 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[C32 (line)]] | wt | 274 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.168× (z -9.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -9.3) |
| [[LS 180 (line)]] | wt | 147 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.330× (z -10.7) ⚠ cell-cycle shift, explains ~51% of this change |
| [[COLO 205 (line)]] | alt | 306 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.13× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 232 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.249× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[hTERT-HPNE (line)]] | wt | 170 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.365× (z -8.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[LOX-IMVI (line)]] | wt | 152 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.315× (z -12.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H2030 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.311× (z -12.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[RKO (line)]] | wt | 259 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[RPMI-7951 (line)]] | alt | 200 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -8.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SNU-1 (line)]] | wt | 180 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SNU-423 (line)]] | alt | 168 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.415× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[BT-474 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 232 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 490 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 183 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 309 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 313 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7243), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP42]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[AKR1C3]] | +0.52 | +0.54 / +0.36 | both halves | 1e-04 |  |
| [[MID1]] | +0.52 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[LUM]] | +0.51 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[LUC7L2]] | +0.51 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[GTF2I]] | +0.51 | +0.36 / +0.55 | both halves | 9e-05 |  |
| [[TNFRSF11B]] | +0.49 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[DIO2]] | +0.49 | +0.48 / +0.40 | both halves | 5e-05 |  |
| [[TNS3]] | +0.48 | +0.41 / +0.40 | both halves | 4e-05 |  |
| [[MTUS1]] | +0.48 | +0.46 / +0.40 | both halves | 5e-05 | same gene group |
| [[AKR1C2]] | +0.48 | +0.44 / +0.32 | both halves | 2e-04 |  |
| [[PBX1]] | +0.47 | +0.49 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP2R2C]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[CAPRIN2]] | -0.49 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[ZNF699]] | -0.47 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[LPAR3]] | -0.47 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[NLRP3]] | -0.47 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[CSGALNACT2]] | -0.46 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[ESAM]] | -0.45 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[ESYT3]] | -0.45 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[GLRX]] | -0.45 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[KIF5A]] | -0.45 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[TOX2]] | -0.45 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[GBX1]] | -0.44 | -0.43 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOX6]] | B | SOX6 activity raises AOPEP's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 1.33× lower at baseline in the lines without SOX6 | 0.058 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers AOPEP's level | compounds that target MAP2K1: 2 of 4 raise it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.8% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.416). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-7.0, 51.0); signed map (53.0, -7.6). **Vector** length 91.5, 31.7% of its response variance represented; |z| ≥ 3 in 1,467 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.1 | -4.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.8 | +0.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -0.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | aminopeptidase O (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.32 — chr9:94,726,604-95,151,793 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C90RF3, FLJ14675, APO, AP-O; previously C9orf3 |
| Gene groups (HGNC) | M1 metallopeptidases; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N6M6](https://www.uniprot.org/uniprotkb/Q8N6M6) (Aminopeptidase O):

> Aminopeptidase which catalyzes the hydrolysis of amino acid residues from the N-terminus of peptide or protein substrates.

**Summary**, from NCBI Gene [84909](https://www.ncbi.nlm.nih.gov/gene/84909):

> This gene encodes a member of the M1 zinc aminopeptidase family. The encoded protein is a zinc-dependent metallopeptidase that catalyzes the removal of an amino acid from the amino terminus of a protein or peptide. This protein may play a role in the generation of angiotensin IV. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Oct 2010]

**Accessions** — [HGNC:1361](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1361) · Entrez [84909](https://www.ncbi.nlm.nih.gov/gene/84909) · UniProt [Q8N6M6](https://www.uniprot.org/uniprotkb/Q8N6M6) · Ensembl [ENSG00000148120](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148120)

## Data

Gene col 7243: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7243); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7243, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7243]; `tensor/DDL_lfc|DDL_z.npy` [7243]; `embed/gene_vectors.npy` [7243]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7243 or target_col == 7243). Every well: [[AOPEP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AOPEP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
