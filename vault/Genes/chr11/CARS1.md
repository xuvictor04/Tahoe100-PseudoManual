---
symbol: "CARS1"
type: "gene"
col: 3149
ensembl_id: "ENSG00000110619"
name: "cysteinyl-tRNA synthetase 1"
location: "11p15.4"
module: 63
arm: "+"
pooled_cpm: 130.58
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 21
n_dd_up_clean: 25
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# CARS1

*cysteinyl-tRNA synthetase 1* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (2 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 1.59× (z +12.9, q 1e-35, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.673× (z -11.1, q 8e-26, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GARS1]] (+0.88, fdr 7e-06), [[ASNS]] (+0.88, fdr 7e-06), [[MARS1]] (+0.87, fdr 7e-06); moves opposite to [[PLPP3]] (-0.52, fdr 2e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ASNSP1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LINC00662]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3149.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **1.59×** | +12.9 | 1e-35 | 45/48 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.76×** | +11.6 | 1e-28 | 43/48 (LOX-IMVI, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +11.0 | 1e-25 | 40/48 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.44×** | +10.4 | 4e-23 | 39/48 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.65×** | +10.3 | 1e-22 | 40/48 (LOX-IMVI, NCI-H2347, …) | all doses, flat |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.48×** | +8.0 | 8e-14 | 43/48 (HEC-1-A, C32, …) | rises with dose | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.47×** | +7.9 | 2e-13 | 36/47 (HEC-1-A, C32, …) | rises with dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.46×** | +7.8 | 4e-13 | 36/48 (LOX-IMVI, Panc 03.27, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.30×** | +7.3 | 2e-11 | 31/49 (Hs 766T, MIA PaCa-2, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.39×** | +6.8 | 6e-10 | 33/48 (LOX-IMVI, C-33 A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.37×** | +6.5 | 4e-09 | 34/48 (Hs 766T, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +6.3 | 1e-08 | 28/47 (AsPC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +6.3 | 2e-08 | 30/49 (COLO 205, CHP-212, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.31×** | +5.5 | 1e-06 | 28/48 (C32, HEC-1-A, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.65×** | +5.4 | 2e-06 | 30/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.59×** | +5.0 | 2e-05 | 30/48 (LOX-IMVI, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.9 | 3e-05 | 24/48 (HOP62, C-33 A, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3149.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.673×** | -11.1 | 8e-26 | 39/48 (J82, HS-578T, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.685×** | -10.5 | 1e-23 | 30/48 (HT-29, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.647×** | -9.0 | 4e-17 | 37/48 (LoVo, HT-29, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.645×** | -8.7 | 4e-16 | 33/47 (HT-29, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.671×** | -8.2 | 2e-14 | 35/48 (H4, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.666×** | -8.1 | 7e-14 | 30/44 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.682×** | -7.9 | 2e-13 | 32/49 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.699×** | -6.8 | 5e-10 | 36/47 (A-172, LoVo, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.718×** | -6.6 | 3e-09 | 27/48 (LoVo, HT-29, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.577×** | -5.9 | 2e-07 | 30/49 (SW1417, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.740×** | -5.8 | 4e-07 | 27/45 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.836× | -5.1 | 2e-05 | 24/48 (HT-29, J82, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.843× | -4.9 | 4e-05 | 21/48 (SW480, PANC-1, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.806×** | -4.5 | 3e-04 | 24/49 (RKO, LS 180, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.810×** | -4.4 | 5e-04 | 23/48 (SW1417, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.816×** | -4.2 | 9e-04 | 22/48 (HS-578T, RPMI-7951, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.819×** | -4.1 | 0.001 | 24/48 (J82, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[AZD-8055 (drug)]] 5 µM |  | **0.703×** | -3.8 | 0.004 | 18/49 (A-172, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.842× | -3.6 | 0.009 | 21/48 (LS 180, SW48, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.846× | -3.5 | 0.012 | 15/48 (SNU-1, HOP62, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.841× | -3.4 | 0.015 | 17/47 (SW1417, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3149. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 259 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -26.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.472× (z -10.8) |
| [[SW1417 (line)]] | alt | 142 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -23.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.394× (z -11.7) |
| [[PANC-1 (line)]] | alt | 402 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.388× (z -14.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 265 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.276× (z -15.1) |
| [[LoVo (line)]] | wt | 157 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -18.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.227× (z -16.8) |
| [[SW480 (line)]] | alt | 192 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -15.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.635× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 107 | 5 (1 ⚠) | 1 (1 ⚠) | [[Neratinib (maleate) (drug)]] 5 µM 1.86× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -17.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 134 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -27.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.545× (z -9.9) |
| [[Hs 766T (line)]] | wt | 166 | 4 | 1 (1 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.32× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.349× (z -11.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 196 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -12.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 154 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 1.94× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -14.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[KATO III (line)]] | alt | 105 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -13.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-1 (line)]] | wt | 155 | 2 | 1 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.37× (z +10.0) | [[Harringtonine (drug)]] 0.05 µM 0.339× (z -8.5) |
| [[A-172 (line)]] | wt | 180 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.572× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 90.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -14.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[C32 (line)]] | wt | 62.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.12× (z +11.5) | — |
| [[HEC-1-A (line)]] | alt | 51.5 | 2 | 0 | [[Artesunate (drug)]] 5 µM 2.61× (z +10.0) | — |
| [[HS-578T (line)]] | alt | 163 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.555× (z -10.1) |
| [[J82 (line)]] | alt | 124 | 1 | 1 | [[Neratinib (maleate) (drug)]] 0.5 µM 2.01× (z +9.0) | [[Selinexor (drug)]] 5 µM 0.479× (z -12.9) |
| [[LS 180 (line)]] | wt | 147 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.354× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 104 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.86× (z +11.0) | — |
| [[NCI-H2347 (line)]] | alt | 98.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.98× (z +8.5) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -10.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RKO (line)]] | wt | 149 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.278× (z -10.4) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 108 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.54× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.366× (z -9.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 95.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -9.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HOP62 (line)]] | alt | 81.9 | 1 | 0 | [[Artesunate (drug)]] 5 µM 1.96× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 88.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -9.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -19.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 66.0 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.89× (z +8.7) | — |
| [[NCI-H661 (line)]] | alt | 94.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -9.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 111 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.30× (z +8.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[A549 (line)]] | wt | 99.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 114 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 99.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3149), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GARS1]] | +0.88 | +0.87 / +0.88 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 894 |
| [[ASNS]] | +0.88 | +0.92 / +0.84 | both halves | 7e-06 | STRING 536 |
| [[MARS1]] | +0.87 | +0.86 / +0.85 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 890 |
| [[AARS1]] | +0.86 | +0.87 / +0.84 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 872 |
| [[SARS1]] | +0.85 | +0.85 / +0.84 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 913 |
| [[MTHFD2]] | +0.83 | +0.84 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[EIF2S2]] | +0.82 | +0.80 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[CHAC1]] | +0.82 | +0.77 / +0.81 | both halves | 7e-06 | STRING 453 |
| [[GOT1]] | +0.81 | +0.77 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[YARS1]] | +0.81 | +0.81 / +0.83 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 898 |
| [[XPOT]] | +0.81 | +0.82 / +0.80 | both halves | 7e-06 |  |
| [[PHGDH]] | +0.81 | +0.82 / +0.79 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLPP3]] | -0.52 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASNSP1]] | B | ASNSP1 activity raises CARS1's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.42× lower at baseline in the lines without ASNSP1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[ULBP1]] | B | ULBP1 activity raises CARS1's level | lines that do not express ULBP1 (15) vs lines expressing it (35) | 1.46× lower at baseline in the lines without ULBP1 | 0.041 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MTOR]] | B | MTOR activity raises CARS1's level | compounds that target MTOR: 4 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Temsirolimus) | 50% of the class's compounds vs 3.6% of all compounds | 0.058 | ⚠ off-target possible; 4 compounds |
| [[ASNSP1]] | B | ASNSP1 activity weakens CARS1's drug response | lines that do not express ASNSP1 (35) vs lines expressing it (13) | the lines without ASNSP1 respond 1.10× as strongly (z diff +0.12); strongest at Neratinib (maleate) 0.5 µM: 1.84x vs 1.38x (z diff -1.9) | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00662]] | C | CARS1's natural level strengthens LINC00662's drug response | CARS1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.66, reverse -0.18; direction not clear | 0.054 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.879). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.3, 48.2); signed map (-13.2, 24.7). **Vector** length 158, 54.8% of its response variance represented; |z| ≥ 3 in 1,486 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mTORC1 signaling* (hallmark, mean cos +0.66 to 20); *unfolded protein response* (hallmark, mean cos +0.74 to 11); *Metabolism of amino acids and derivatives* (reactome, mean cos +0.68 to 14).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM |  | +10.8 | +12.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +10.0 | +11.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +8.8 | +7.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.7 | +10.3 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +8.3 | +11.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +8.2 | +10.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +7.1 | +8.0 |
|  | [[Neratinib (drug)]] 5 µM |  | +6.7 | +6.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.9 | -11.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.4 | -9.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -6.4 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.3 | -8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.2 | -5.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.8 | -4.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.6 | -3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.5 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | cysteinyl-tRNA synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:3,000,922-3,057,613 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CARS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class I |
| Reactome | 6 pathways, smallest: Cytosolic tRNA aminoacylation; tRNA Aminoacylation; Signaling by ALK fusions and activated point mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [P49589](https://www.uniprot.org/uniprotkb/P49589) (Cysteine--tRNA ligase, cytoplasmic):

> Catalyzes the ATP-dependent ligation of cysteine to tRNA(Cys).

**Summary**, from NCBI Gene [833](https://www.ncbi.nlm.nih.gov/gene/833):

> This gene encodes a class 1 aminoacyl-tRNA synthetase, cysteinyl-tRNA synthetase. Each of the twenty aminoacyl-tRNA synthetases catalyzes the aminoacylation of a specific tRNA or tRNA isoaccepting family with the cognate amino acid. This gene is one of several located near the imprinted gene domain on chromosome 11p15.5, an important tumor-suppressor gene region. Alterations in this region have been associated with Beckwith-Wiedemann syndrome, Wilms tumor, rhabdomyosarcoma, adrenocortical …

**Accessions** — [HGNC:1493](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1493) · Entrez [833](https://www.ncbi.nlm.nih.gov/gene/833) · UniProt [P49589](https://www.uniprot.org/uniprotkb/P49589) · Ensembl [ENSG00000110619](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110619)

## Data

Gene col 3149: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3149); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3149, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3149]; `tensor/DDL_lfc|DDL_z.npy` [3149]; `embed/gene_vectors.npy` [3149]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3149 or target_col == 3149). Every well: [[CARS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CARS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
