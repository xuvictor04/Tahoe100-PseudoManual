---
symbol: "TCEA1"
type: "gene"
col: 11940
ensembl_id: "ENSG00000187735"
name: "transcription elongation factor A1"
location: "8q11.23"
module: 63
arm: "+"
pooled_cpm: 121.47
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 11
n_dd_up_clean: 18
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# TCEA1

*transcription elongation factor A1* — 8q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.85× (z +11.6, q 8e-29, up in 42 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Artesunate (drug)]] 5 µM: 1.59× (z +11.6, q 8e-29, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.816× (z -5.1, q 1e-04, down in 25 of 49 measured lines) ⚠ cell-cycle shift, explains ~19% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.805× (z -4.1, q 0.004, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPRS1]] (+0.86, fdr 7e-06), [[XPOT]] (+0.85, fdr 7e-06), [[PSAT1]] (+0.84, fdr 7e-06); moves opposite to [[POLR2L]] (-0.58, fdr 1e-05), [[TUBB4B]] (-0.55, fdr 1e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ASNSP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11940.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +11.6 | 8e-29 | 42/49 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 5 µM |  | **1.59×** | +11.6 | 8e-29 | 43/48 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +10.8 | 4e-25 | 43/47 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +9.8 | 1e-20 | 35/44 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 0.5 µM |  | **1.55×** | +8.3 | 1e-14 | 39/48 (SNU-1, SW480, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.46×** | +7.1 | 1e-10 | 31/48 (SW480, LoVo, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +6.5 | 6e-09 | 35/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +6.4 | 9e-09 | 33/45 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.39×** | +6.2 | 4e-08 | 34/47 (SNU-1, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +6.2 | 4e-08 | 32/48 (NCI-H460, C32, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.24×** | +5.4 | 3e-06 | 30/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.71×** | +5.3 | 5e-06 | 32/48 (LOX-IMVI, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.30×** | +5.0 | 3e-05 | 31/48 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.64×** | +4.9 | 5e-05 | 30/48 (NCI-H460, BT-474, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.29×** | +4.7 | 8e-05 | 25/48 (BT-474, SNU-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +4.7 | 1e-04 | 28/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.28×** | +4.6 | 1e-04 | 28/48 (SW480, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +4.4 | 4e-04 | 24/48 (LoVo, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.55×** | +4.3 | 4e-04 | 31/48 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +4.2 | 9e-04 | 22/49 (COLO 205, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11940.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.816×** | -5.1 | 1e-04 | 25/49 (PANC-1, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.779×** | -4.7 | 6e-04 | 25/48 (PANC-1, KATO III, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.797×** | -4.3 | 0.003 | 29/48 (LoVo, KATO III, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.803×** | -4.2 | 0.004 | 26/48 (PANC-1, KATO III, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -4.1 | 0.004 | 24/48 (HT-29, PANC-1, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.805×** | -4.1 | 0.004 | 24/48 (HT-29, LoVo, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.808×** | -4.0 | 0.004 | 27/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.807×** | -3.9 | 0.007 | 21/47 (KATO III, HT-29, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.862× | -3.8 | 0.011 | 22/48 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.823×** | -3.7 | 0.013 | 23/48 (HT-29, AsPC-1, …) | two highest doses | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.815×** | -3.6 | 0.017 | 26/47 (H4, LoVo, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | **0.828×** | -3.4 | 0.028 | 22/48 (HT-29, PANC-1, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.847× | -3.2 | 0.068 | 21/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | 0.847× | -3.1 | 0.068 | 22/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.849× | -3.1 | 0.073 | 14/48 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.851× | -3.1 | 0.074 | 13/49 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.846× | -3.0 | 0.074 | 18/48 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Ritonavir (drug)]] 5 µM |  | 0.885× | -3.0 | 0.074 | 3/48 (Hs 766T, SNU-1, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.801×** | -3.0 | 0.080 | 17/48 (SK-MEL-2, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.855× | -3.0 | 0.086 | 15/48 (LoVo, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11940. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 101 | 7 (4 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.50× (z +14.8) ⚠ toxic · without an alert: [[Artesunate (drug)]] 5 µM 1.81× (z +13.2) | — |
| [[LoVo (line)]] | wt | 127 | 5 (1 ⚠) | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.28× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.556× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 197 | 2 | 4 (4 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.78× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.505× (z -10.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HT-29 (line)]] | alt | 168 | 1 | 4 (3 ⚠) | [[Artesunate (drug)]] 5 µM 1.76× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.465× (z -9.5) |
| [[SNU-1 (line)]] | wt | 159 | 5 (1 ⚠) | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 3.95× (z +17.0) | — |
| [[HEC-1-A (line)]] | alt | 116 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Artesunate (drug)]] 5 µM 2.01× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 91.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +12.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 108 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +10.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 199 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.402× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[RKO (line)]] | wt | 127 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.65× (z +11.4) ⚠ toxic · without an alert: [[Artesunate (drug)]] 5 µM 1.98× (z +11.1) | — |
| [[AN3 CA (line)]] | alt | 132 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 3.29× (z +8.5) ⚠ toxic | [[Decitabine (drug)]] 0.05 µM 0.202× (z -11.1) |
| [[COLO 205 (line)]] | alt | 72.4 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.33× (z +11.3) ⚠ toxic | — |
| [[NCI-H23 (line)]] | alt | 105 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.43× (z +10.2) ⚠ toxic | — |
| [[NCI-H460 (line)]] | wt | 59.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 107 | 2 | 0 | [[Artesunate (drug)]] 5 µM 2.14× (z +12.1) | — |
| [[AsPC-1 (line)]] | alt | 99.2 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.78× (z +11.0) ⚠ toxic | — |
| [[BT-474 (line)]] | alt | 71.1 | 1 | 0 | [[Artesunate (drug)]] 5 µM 2.24× (z +10.7) | — |
| [[C32 (line)]] | wt | 96.5 | 1 | 0 | [[Artesunate (drug)]] 5 µM 1.83× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 99.9 | 1 | 0 | [[Artesunate (drug)]] 5 µM 2.15× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 95.3 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.42× (z +10.1) ⚠ toxic | — |
| [[Hs 766T (line)]] | wt | 89.6 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.73× (z +9.2) ⚠ toxic | — |
| [[J82 (line)]] | alt | 118 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.56× (z +10.2) ⚠ toxic | — |
| [[LOX-IMVI (line)]] | wt | 103 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.39× (z +10.2) ⚠ toxic | — |
| [[MIA PaCa-2 (line)]] | alt | 173 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.99× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 83.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +8.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 94.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 125 | 1 | 0 | [[Artesunate (drug)]] 5 µM 2.41× (z +9.2) | — |
| [[A-172 (line)]] | wt | 85.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 213 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 116 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 83.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 159 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 70.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 310 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 70.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11940), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPRS1]] | +0.86 | +0.87 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[XPOT]] | +0.85 | +0.83 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[PSAT1]] | +0.84 | +0.77 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[ZFAND1]] | +0.82 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[AARS1]] | +0.81 | +0.78 / +0.81 | both halves | 7e-06 |  |
| [[NARS1]] | +0.81 | +0.74 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[TARS1]] | +0.81 | +0.79 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[MTHFD2]] | +0.80 | +0.74 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[RSL24D1]] | +0.79 | +0.79 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[PHGDH]] | +0.79 | +0.74 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[GARS1]] | +0.78 | +0.81 / +0.75 | both halves | 7e-06 |  |
| [[SARS1]] | +0.77 | +0.80 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2L]] | -0.58 | -0.64 / -0.53 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins; STRING 986 |
| [[TUBB4B]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASNSP1]] | B | ASNSP1 activity raises TCEA1's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.27× lower at baseline in the lines without ASNSP1 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.850). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.8, 47.3); signed map (-14.2, 24.1). **Vector** length 148, 50.6% of its response variance represented; |z| ≥ 3 in 1,152 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.67 to 16); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.78 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.78 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM |  | +9.2 | +11.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +9.1 | +6.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +7.4 | +5.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +7.1 | +8.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.1 | +10.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +6.1 | +7.1 |
|  | [[Neratinib (drug)]] 5 µM |  | +5.9 | +3.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -7.5 | -4.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -7.2 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -6.1 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -5.9 | -3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.8 | -4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.4 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -3.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.5 | -2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.4 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | transcription elongation factor A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q11.23 — chr8:53,966,552-54,022,448 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SII, TF2S, TFIIS; previously TCEA, GTF2S |
| Gene groups (HGNC) | General transcription factors |
| Hallmark sets | HEME_METABOLISM, MTORC1_SIGNALING |
| Reactome | 28 pathways, smallest: Pausing and recovery of Tat-mediated HIV elongation; Tat-mediated HIV elongation arrest and recovery; HIV elongation arrest and recovery |
| Matched by | ensembl_id |

**Function**, from UniProt [P23193](https://www.uniprot.org/uniprotkb/P23193) (Transcription elongation factor A protein 1):

> Necessary for efficient RNA polymerase II transcription elongation past template-encoded arresting sites. The arresting sites in DNA have the property of trapping a certain fraction of elongating RNA polymerases that pass through, resulting in locked ternary complexes. Cleavage of the nascent transcript by S-II allows the resumption of elongation from the new 3'-terminus.

**Summary**, from NCBI Gene [6917](https://www.ncbi.nlm.nih.gov/gene/6917):

> Enables transcription elongation factor activity. Involved in transcription elongation by RNA polymerase II. Located in nucleoplasm. Part of transcription factor TFIID complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11612](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11612) · Entrez [6917](https://www.ncbi.nlm.nih.gov/gene/6917) · UniProt [P23193](https://www.uniprot.org/uniprotkb/P23193) · Ensembl [ENSG00000187735](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187735)

## Data

Gene col 11940: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11940); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11940, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11940]; `tensor/DDL_lfc|DDL_z.npy` [11940]; `embed/gene_vectors.npy` [11940]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11940 or target_col == 11940). Every well: [[TCEA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCEA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
