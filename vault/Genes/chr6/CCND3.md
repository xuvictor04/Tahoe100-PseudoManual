---
symbol: "CCND3"
type: "gene"
col: 3381
ensembl_id: "ENSG00000112576"
name: "cyclin D3"
location: "6p21.1"
module: 98
arm: "+"
pooled_cpm: 26.86
n_lines_expressing: 49
n_dd_up: 45
n_dd_down: 27
n_dd_up_clean: 38
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# CCND3

*cyclin D3* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (7 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 3.88× (z +18.5, q 0e+00, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.459× (z -10.6, q 1e-23, down in 40 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 0.557× (z -7.5, q 1e-11, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FKBP5]] (+0.73, fdr 7e-06), [[KLF9]] (+0.71, fdr 7e-06), [[MAOA]] (+0.71, fdr 7e-06); moves opposite to [[ADAMTS16]] (-0.64, fdr 7e-06), [[PTHLH]] (-0.58, fdr 1e-05), [[SIRLNT]] (-0.58, fdr 1e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[SAA1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 7 with an alert ⚠; shown: the 15 strongest. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3381.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **3.88×** | +18.5 | 0e+00 | 42/46 (PANC-1, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **3.46×** | +16.9 | 0e+00 | 31/47 (HOP62, PANC-1, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **2.20×** | +15.2 | 0e+00 | 33/47 (HOP62, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **2.98×** | +14.8 | 0e+00 | 33/47 (HOP62, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **2.89×** | +14.4 | 4e-45 | 31/46 (SK-MEL-2, PANC-1, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **2.82×** | +14.1 | 2e-43 | 31/47 (HOP62, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **2.78×** | +13.9 | 5e-42 | 32/47 (HOP62, PANC-1, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.64×** | +13.2 | 5e-38 | 32/46 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **2.52×** | +12.6 | 1e-34 | 31/47 (HOP62, PANC-1, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **2.50×** | +12.5 | 6e-34 | 33/47 (HOP62, CFPAC-1, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **2.47×** | +12.3 | 6e-33 | 31/47 (HOP62, PANC-1, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.52×** | +12.1 | 7e-32 | 32/46 (HOP62, PANC-1, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **2.32×** | +11.4 | 1e-28 | 29/47 (PANC-1, SK-MEL-2, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **2.26×** | +11.1 | 4e-27 | 30/46 (HOP62, PANC-1, …) | all doses, flat |  |
| [[Econazole (drug)]] 5 µM |  | **2.26×** | +11.1 | 4e-27 | 30/47 (PANC-1, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3381.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.459×** | -10.6 | 1e-23 | 40/47 (SW480, Panc 03.27, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.557×** | -7.5 | 1e-11 | 28/47 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.662×** | -5.6 | 4e-06 | 24/46 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.766×** | -5.1 | 3e-05 | 27/47 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.767×** | -5.1 | 3e-05 | 25/46 (COLO 205, SW1417, …) | rises with dose | composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.493×** | -5.0 | 4e-05 | 22/46 (SW1417, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.696×** | -4.9 | 6e-05 | 23/47 (BT-474, HT-29, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.500×** | -4.9 | 6e-05 | 21/47 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.505×** | -4.9 | 7e-05 | 22/46 (SW480, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.714×** | -4.6 | 2e-04 | 17/47 (SW1417, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.728×** | -4.3 | 8e-04 | 21/46 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.546×** | -4.3 | 8e-04 | 21/47 (NCI-H1792, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.671×** | -3.9 | 0.004 | 17/47 (SW480, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.586×** | -3.8 | 0.006 | 18/46 (BT-474, NCI-H661, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.761×** | -3.6 | 0.013 | 19/46 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.761×** | -3.5 | 0.015 | 19/47 (SK-MEL-2, SW1417, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.774×** | -3.5 | 0.016 | 14/46 (SW 900, SK-MEL-2, …) | two highest doses | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **0.616×** | -3.4 | 0.017 | 15/46 (SW480, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3381. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 101 | 20 | 4 (4 ⚠) | [[Triamcinolone (drug)]] 5 µM 3.14× (z +13.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.232× (z -12.0) ⚠ cell-cycle shift, explains ~78% of this change |
| [[PANC-1 (line)]] | alt | 15.9 | 21 (1 ⚠) | 1 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 7.84× (z +14.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.266× (z -9.6) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 13.6 | 21 (1 ⚠) | 0 | [[Triamcinolone (drug)]] 5 µM 6.91× (z +12.9) | — |
| [[CFPAC-1 (line)]] | alt | 37.8 | 20 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 9.75× (z +13.3) | — |
| [[HOP62 (line)]] | alt | 29.7 | 20 | 0 | [[Triamcinolone (drug)]] 5 µM 6.02× (z +16.8) | — |
| [[NCI-H1573 (line)]] | alt | 26.9 | 18 (1 ⚠) | 1 (1 ⚠) | [[Quinestrol (drug)]] 5 µM 4.99× (z +12.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -9.8) ⚠ cell-cycle shift, explains ~78% of this change |
| [[SK-MEL-2 (line)]] | alt | 27.7 | 18 | 1 | [[Triamcinolone (drug)]] 5 µM 5.65× (z +13.2) | [[Ixazomib citrate (drug)]] 0.5 µM 0.172× (z -9.5) |
| [[SNU-423 (line)]] | alt | 28.1 | 16 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 10.1× (z +12.5) | — |
| [[LoVo (line)]] | wt | 22.5 | 5 | 3 (1 ⚠) | [[Triamcinolone (drug)]] 5 µM 2.68× (z +9.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.252× (z -9.5) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.271× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 20.2 | 8 | 0 | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 4.46× (z +9.7) | — |
| [[Hs 766T (line)]] | wt | 18.7 | 6 | 0 | [[Triamcinolone (drug)]] 5 µM 4.82× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 13.7 | 5 | 0 | [[Triamcinolone (drug)]] 5 µM 4.33× (z +10.1) | — |
| [[SW 900 (line)]] | alt | 34.3 | 5 | 0 | [[Clobetasol propionate (drug)]] 5 µM 8.08× (z +10.2) | — |
| [[COLO 205 (line)]] | alt | 135 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -12.3) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.304× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 35.5 | 4 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 6.10× (z +11.5) | — |
| [[A549 (line)]] | wt | 22.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Triamcinolone (drug)]] 5 µM 3.09× (z +8.7) | — |
| [[LOX-IMVI (line)]] | wt | 9.44 | 3 (1 ⚠) | 0 | [[Clobetasol propionate (drug)]] 5 µM 7.65× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 39.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -10.3) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.290× (z -10.3) |
| [[SW480 (line)]] | alt | 32.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.36× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.32× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.223× (z -15.1) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 10.4 | 2 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 13.0× (z +10.7) | — |
| [[NCI-H2030 (line)]] | alt | 43.7 | 2 | 0 | [[Triamcinolone (drug)]] 5 µM 2.33× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 16.7 | 2 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 9.67× (z +9.3) | — |
| [[A-172 (line)]] | wt | 24.7 | 1 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 4.65× (z +8.9) | — |
| [[A-427 (line)]] | wt | 16.7 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.29× (z +9.1) | — |
| [[A498 (line)]] | wt | 34.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.376× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 21.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.48× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[HT-29 (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.257× (z -10.0) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -9.5) ⚠ cell-cycle shift, explains ~23% of this change |
| [[AN3 CA (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3381), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKBP5]] | +0.73 | +0.75 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[KLF9]] | +0.71 | +0.75 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[MAOA]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[COPS8]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[TLR2]] | +0.67 | +0.65 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[SAA1]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[ZMYND8]] | +0.65 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[PID1]] | +0.65 | +0.70 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[TNS2]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[MT1E]] | +0.63 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[MT1M]] | +0.63 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[DNER]] | +0.63 | +0.65 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS16]] | -0.64 | -0.70 / -0.62 | both halves | 7e-06 | **novel candidate** |
| [[PTHLH]] | -0.58 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[SIRLNT]] | -0.58 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[KCNMA1]] | -0.54 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[ANXA10]] | -0.52 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[LINC00536]] | -0.51 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[GCKR]] | -0.51 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[RABGEF1P3]] | -0.50 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[LINC01411]] | -0.49 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[IGFN1]] | -0.49 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[MRPS6]] | -0.49 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[LRRC49]] | -0.49 | -0.45 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAA1]] | B | SAA1 activity raises CCND3's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 1.58× lower at baseline in the lines without SAA1 | 0.013 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11 |
| [[HS3ST3B1]] | B | HS3ST3B1 activity lowers CCND3's level | lines that do not express HS3ST3B1 (18) vs lines expressing it (32) | 1.42× higher at baseline in the lines without HS3ST3B1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| [[SAA2-SAA4]], [[SAA4]] | B | SAA2-SAA4, SAA4 activity raises CCND3's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 1.58× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.046 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[SERPINA5]] | B | SERPINA5 activity raises CCND3's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 1.57× lower at baseline in the lines without SERPINA5 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |
| [[SAA2]] | B | SAA2 activity raises CCND3's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 1.48× lower at baseline in the lines without SAA2 | 0.068 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3 |
| [[SLC7A2]] | B | SLC7A2 activity lowers CCND3's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 1.21× higher at baseline in the lines without SLC7A2 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D |
| [[NR3C1]] | B | NR3C1 activity raises CCND3's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.7% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[SLC26A2]] | C | SLC26A2 activity lowers CCND3's level | lines that do not express SLC26A2 (4) vs lines expressing it (46) | 2.02× higher at baseline in the lines without SLC26A2 | 0.0997 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MIR4435-2HG, EPB41L2, CEP85L; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.752). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.2, 15.5); signed map (17.0, 30.8). **Vector** length 127, 38.9% of its response variance represented; |z| ≥ 3 in 1,717 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Clobetasol propionate (drug)]] 0.05 µM |  | +8.7 | +18.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +7.6 | +15.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +7.5 | +14.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +7.5 | +14.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +7.5 | +12.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.1 | -10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.2 | +0.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.6 | -3.4 |
|  | [[EX229 (drug)]] 5 µM |  | -4.5 | -5.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.3 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.2 | -4.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | cyclin D3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:41,934,934-42,050,357 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cyclins |
| Hallmark sets | ANDROGEN_RESPONSE, ALLOGRAFT_REJECTION, UV_RESPONSE_UP, IL2_STAT5_SIGNALING, HEME_METABOLISM, P53_PATHWAY |
| Reactome | 16 pathways, smallest: Drug-mediated inhibition of CDK4/CDK6 activity; Aberrant regulation of mitotic G1/S transition in cancer due to RB1 defects; Defective binding of RB1 mutants to E2F1,(E2F2, E2F3) |
| Matched by | ensembl_id |

**Function**, from UniProt [P30281](https://www.uniprot.org/uniprotkb/P30281) (G1/S-specific cyclin-D3):

> Regulatory component of the cyclin D3-CDK4 (DC) complex that phosphorylates and inhibits members of the retinoblastoma (RB) protein family including RB1 and regulates the cell-cycle during G(1)/S transition. Phosphorylation of RB1 allows dissociation of the transcription factor E2F from the RB/E2F complex and the subsequent transcription of E2F target genes which are responsible for the progression through the G(1) phase. Hypophosphorylates RB1 in early G(1) phase. Cyclin D-CDK4 complexes are …

**Summary**, from NCBI Gene [896](https://www.ncbi.nlm.nih.gov/gene/896):

> The protein encoded by this gene belongs to the highly conserved cyclin family, whose members are characterized by a dramatic periodicity in protein abundance through the cell cycle. Cyclins function as regulators of CDK kinases. Different cyclins exhibit distinct expression and degradation patterns which contribute to the temporal coordination of each mitotic event. This cyclin forms a complex with and functions as a regulatory subunit of CDK4 or CDK6, whose activtiy is required for cell cycle …

**Accessions** — [HGNC:1585](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1585) · Entrez [896](https://www.ncbi.nlm.nih.gov/gene/896) · UniProt [P30281](https://www.uniprot.org/uniprotkb/P30281) · Ensembl [ENSG00000112576](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112576)

## Data

Gene col 3381: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3381); `tables/drug_effects.parquet` (77 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3381, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3381]; `tensor/DDL_lfc|DDL_z.npy` [3381]; `embed/gene_vectors.npy` [3381]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3381 or target_col == 3381). Every well: [[CCND3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCND3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
