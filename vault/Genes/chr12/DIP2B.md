---
symbol: "DIP2B"
type: "gene"
col: 817
ensembl_id: "ENSG00000066084"
name: "DIP2 acetate--CoA ligase B (putative)"
location: "12q13.12"
module: 56
arm: "+"
pooled_cpm: 198.97
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# DIP2B

*DIP2 acetate--CoA ligase B (putative)* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.70× (z +9.6, q 3e-19, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.525× (z -16.5, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A13]] (+0.52, fdr 8e-05), [[ATP9B]] (+0.51, fdr 5e-05), [[OSBP2]] (+0.50, fdr 4e-05); moves opposite to [[DNAJC25]] (-0.57, fdr 1e-05), [[SUCO]] (-0.53, fdr 1e-04), [[GOLT1B]] (-0.53, fdr 2e-04).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 817.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +9.6 | 3e-19 | 43/48 (NCI-H1792, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +7.0 | 8e-10 | 34/48 (NCI-H1792, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +6.8 | 2e-09 | 40/48 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +6.3 | 5e-08 | 37/48 (NCI-H1573, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +5.9 | 3e-07 | 25/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.57×** | +4.2 | 0.002 | 27/49 (SW480, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +4.2 | 0.002 | 34/48 (C32, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.003 | 25/48 (HEC-1-A, C-33 A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 1.14× | +3.3 | 0.070 | 12/48 (RPMI-7951, PANC-1, …) | rises with dose | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.071 | 21/48 (A-427, hTERT-HPNE, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.081 | 21/48 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.1 | 0.11 | 19/48 (RKO, hTERT-HPNE, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 817.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.525×** | -16.5 | 0e+00 | 44/49 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.409×** | -15.6 | 0e+00 | 41/44 (NCI-H23, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.433×** | -15.1 | 0e+00 | 46/49 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.517×** | -11.1 | 3e-26 | 39/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.670×** | -7.2 | 5e-11 | 38/48 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.667×** | -7.0 | 2e-10 | 38/50 (NCI-H23, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.697×** | -6.3 | 2e-08 | 37/48 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.735×** | -5.6 | 2e-06 | 30/48 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.761×** | -5.0 | 5e-05 | 31/48 (NCI-H2030, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.802×** | -4.0 | 0.004 | 27/48 (HepG2/C3A, CFPAC-1, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.745×** | -3.7 | 0.013 | 27/47 (CHP-212, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.878× | -3.3 | 0.038 | 13/48 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.880× | -3.3 | 0.045 | 5/48 (CFPAC-1, SK-MEL-2, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.838× | -3.2 | 0.054 | 19/48 (C-33 A, CFPAC-1, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.782×** | -3.0 | 0.086 | 17/48 (NCI-H2030, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 817. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 276 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -22.1) |
| [[SW480 (line)]] | alt | 234 | 2 | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 251 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -20.0) |
| [[AsPC-1 (line)]] | alt | 326 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.15× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -19.5) |
| [[HepG2_C3A (line)]] | wt | 411 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -18.5) |
| [[NCI-H1573 (line)]] | alt | 280 | 3 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 321 | 1 | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -18.6) |
| [[C32 (line)]] | wt | 206 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -13.4) |
| [[LS 180 (line)]] | wt | 326 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 242 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0622× (z -32.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -17.6) |
| [[Panc 03.27 (line)]] | alt | 245 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -14.8) |
| [[SW1417 (line)]] | alt | 189 | 1 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -16.1) |
| [[HEC-1-A (line)]] | alt | 107 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.43× (z +12.0) | — |
| [[Hs 766T (line)]] | wt | 90.9 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 148 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +22.7) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -12.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 177 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -14.3) |
| [[A498 (line)]] | wt | 207 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -15.3) |
| [[HT-29 (line)]] | alt | 173 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -9.9) |
| [[KATO III (line)]] | alt | 199 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.606× (z -8.9) |
| [[LoVo (line)]] | wt | 271 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -20.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 166 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -10.4) |
| [[PANC-1 (line)]] | alt | 180 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -9.1) |
| [[RKO (line)]] | wt | 198 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.452× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~21% of this change |
| [[SW 900 (line)]] | alt | 145 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.372× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -9.4) |
| [[SW48 (line)]] | wt | 157 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -8.5) |
| [[A-172 (line)]] | wt | 169 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -14.2) |
| [[A-427 (line)]] | wt | 385 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -15.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 184 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -15.5) |
| [[AN3 CA (line)]] | alt | 273 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -11.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 288 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -13.8) |
| [[C-33 A (line)]] | alt | 154 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -17.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 138 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0746× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -12.0) |
| [[COLO 205 (line)]] | alt | 298 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -17.2) |
| [[HOP62 (line)]] | alt | 109 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.387× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -9.7) |
| [[J82 (line)]] | alt | 116 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +14.3) | — |
| [[RPMI-7951 (line)]] | alt | 93.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -8.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 144 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -12.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 214 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -9.8) |
| [[HS-578T (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.357× (z -10.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 122 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 121 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -10.0) |
| [[NCI-H661 (line)]] | alt | 224 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -9.4) |
| [[SW 1088 (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0879× (z -10.8) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 240 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -8.5) |
| [[H4 (line)]] | wt | 90.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 93.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 128 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 817), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*30 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A13]] | +0.52 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[ATP9B]] | +0.51 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[OSBP2]] | +0.50 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[ATXN7L1]] | +0.49 | +0.29 / +0.55 | both halves | 2e-04 |  |
| [[SLC36A1]] | +0.48 | +0.30 / +0.42 | both halves | 2e-04 |  |
| [[DNAH14]] | +0.47 | +0.29 / +0.41 | both halves | 2e-04 |  |
| [[RABEP1]] | +0.47 | +0.41 / +0.37 | both halves | 8e-05 |  |
| [[CRADD]] | +0.47 | +0.25 / +0.48 | both halves | 4e-04 |  |
| [[GPATCH8]] | +0.45 | +0.36 / +0.41 | both halves | 1e-04 |  |
| [[EPHB2]] | +0.44 | +0.40 / +0.32 | both halves | 2e-04 |  |
| [[MTA3]] | +0.44 | +0.31 / +0.55 | both halves | 2e-04 |  |
| [[PARD3]] | +0.44 | +0.56 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*70 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC25]] | -0.57 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[SUCO]] | -0.53 | -0.34 / -0.60 | both halves | 1e-04 |  |
| [[GOLT1B]] | -0.53 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[MCEE]] | -0.52 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[VDAC1P8]] | -0.52 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[EEF1AKMT3]] | -0.51 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[SAP30-DT]] | -0.49 | -0.25 / -0.59 | both halves | 4e-04 |  |
| [[PRSS53]] | -0.49 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[EOLA1]] | -0.49 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[TXNDC11]] | -0.49 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[HYPK]] | -0.49 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[COPG1]] | -0.49 | -0.42 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DIP2B's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction -0.476). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.3, -34.9); signed map (9.9, -1.8). **Vector** length 98.4, 32.6% of its response variance represented; |z| ≥ 3 in 1,308 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +5.8 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.3 | +3.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +3.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +3.9 | +1.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.6 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | -1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -16.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -7.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -1.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.4 | -1.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.3 | -2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | -1.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | DIP2 acetate--CoA ligase B (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:50,504,985-50,748,657 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1463, FLJ34278 |
| Gene groups (HGNC) | DIP2 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P265](https://www.uniprot.org/uniprotkb/Q9P265) (Disco-interacting protein 2 homolog B):

> Negatively regulates axonal outgrowth and is essential for normal synaptic transmission. Not required for regulation of axon polarity. Promotes acetylation of alpha-tubulin.

**Summary**, from NCBI Gene [57609](https://www.ncbi.nlm.nih.gov/gene/57609):

> This gene encodes a member of the disco-interacting protein homolog 2 protein family. The encoded protein contains a binding site for the transcriptional regulator DNA methyltransferase 1 associated protein 1 as well as AMP-binding sites. The presence of these sites suggests that the encoded protein may participate in DNA methylation. This gene is located near a folate-sensitive fragile site, and CGG-repeat expansion in the promoter of this gene which affects transcription has been detected in …

**Accessions** — [HGNC:29284](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29284) · Entrez [57609](https://www.ncbi.nlm.nih.gov/gene/57609) · UniProt [Q9P265](https://www.uniprot.org/uniprotkb/Q9P265) · Ensembl [ENSG00000066084](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066084)

## Data

Gene col 817: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 817); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 817, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 817]; `tensor/DDL_lfc|DDL_z.npy` [817]; `embed/gene_vectors.npy` [817]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 817 or target_col == 817). Every well: [[DIP2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIP2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
