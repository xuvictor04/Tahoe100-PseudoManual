---
symbol: "PDCL3P4"
type: "gene"
col: 14390
ensembl_id: "ENSG00000244119"
name: "PDCL3 pseudogene 4"
location: "3q12.3"
module: 10
arm: "+"
pooled_cpm: 12.94
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 18
n_dd_up_clean: 36
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# PDCL3P4

*PDCL3 pseudogene 4* — 3q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.12× (z +24.0, q 0e+00, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.314× (z -12.0, q 1e-30, down in 35 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.343× (z -11.1, q 3e-26, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LEKR1]] (+0.85, fdr 7e-06), [[LINC02340]] (+0.83, fdr 7e-06), [[PCNX4-DT]] (+0.81, fdr 8e-06); moves opposite to [[PACC1]] (-0.70, fdr 4e-05), [[L2HGDH]] (-0.67, fdr 4e-05), [[KLHL8]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14390.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.12×** | +24.0 | 0e+00 | 43/45 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.98×** | +16.0 | 0e+00 | 44/46 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.25×** | +12.2 | 5e-32 | 37/45 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.88×** | +11.0 | 8e-26 | 39/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.84×** | +8.9 | 4e-17 | 38/48 (A-427, NCI-H2347, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +8.0 | 8e-14 | 35/43 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.14×** | +7.9 | 2e-13 | 34/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.98×** | +7.1 | 9e-11 | 30/47 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.43×** | +5.2 | 1e-05 | 20/48 (J82, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +5.0 | 4e-05 | 6/18 (HEC-1-A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +4.9 | 4e-05 | 21/46 (HT-29, C-33 A, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +4.6 | 2e-04 | 23/47 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +4.2 | 0.001 | 12/29 (AsPC-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.52×** | +4.2 | 0.001 | 15/47 (SW480, NCI-H460, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +4.1 | 0.001 | 19/48 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.008 | 12/48 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.010 | 18/47 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.010 | 19/47 (NCI-H2347, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14390.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.314×** | -12.0 | 1e-30 | 35/44 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.343×** | -11.1 | 3e-26 | 37/48 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.416×** | -9.1 | 1e-17 | 35/47 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.454×** | -8.2 | 3e-14 | 33/47 (COLO 205, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.455×** | -8.2 | 3e-14 | 31/47 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.574×** | -5.8 | 7e-07 | 26/47 (H4, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.571×** | -5.5 | 3e-06 | 25/48 (HT-29, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.626×** | -4.9 | 7e-05 | 24/48 (PANC-1, A498, …) | two highest doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.607×** | -4.4 | 7e-04 | 22/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.477×** | -4.0 | 0.003 | 18/43 (COLO 205, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.681×** | -3.8 | 0.006 | 20/40 (NCI-H23, A-427, …) | two highest doses | cell-cycle shift (explains ~23% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.647×** | -3.8 | 0.006 | 19/47 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.508×** | -3.7 | 0.010 | 14/44 (CFPAC-1, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.797×** | -3.4 | 0.032 | 15/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.727×** | -3.3 | 0.034 | 15/47 (RPMI-7951, Hs 766T, …) | inconsistent across doses |  |
| [[Fluvoxamine (maleate) (drug)]] 5 µM |  | **0.816×** | -3.0 | 0.087 | 8/48 (NCI-H661, A-172, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.743×** | -3.0 | 0.091 | 13/48 (LOX-IMVI, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14390. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 14.5 | 2 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +13.0) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.117× (z -13.7) |
| [[A-427 (line)]] | wt | 15.9 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 9.21× (z +12.7) | [[Digitoxin (drug)]] 0.5 µM 0.0770× (z -14.7) |
| [[COLO 205 (line)]] | alt | 35.6 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +8.7) | [[Digitoxin (drug)]] 0.5 µM 0.0603× (z -15.9) |
| [[PANC-1 (line)]] | alt | 20.0 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +11.8) | [[Digitoxin (drug)]] 5 µM 0.0992× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.235× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 26.5 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.27× (z +16.4) | [[Digitoxin (drug)]] 5 µM 0.0785× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.167× (z -10.4) |
| [[LoVo (line)]] | wt | 15.6 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 8.10× (z +17.3) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.191× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 16.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.76× (z +15.0) | — |
| [[Hs 766T (line)]] | wt | 16.8 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +12.8) | [[Ixazomib citrate (drug)]] 5 µM 0.141× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 11.5 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.64× (z +13.6) | [[Ixazomib citrate (drug)]] 5 µM 0.0742× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 24.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.95× (z +18.9) | [[Digitoxin (drug)]] 5 µM 0.0230× (z -24.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 6.28 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +13.4) | [[Digitoxin (drug)]] 5 µM 0.105× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 9.87 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.07× (z +11.1) | — |
| [[A498 (line)]] | wt | 4.77 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 12.3× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 8.02 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +13.4) | — |
| [[C-33 A (line)]] | alt | 11.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +8.6) | [[Digitoxin (drug)]] 0.05 µM 0.0602× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 18.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.143× (z -10.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 16.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +8.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -9.8) |
| [[J82 (line)]] | alt | 6.42 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.0838× (z -10.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 12.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +11.3) | — |
| [[NCI-H460 (line)]] | wt | 7.16 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.74× (z +15.8) | — |
| [[A-172 (line)]] | wt | 15.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +9.2) | — |
| [[A549 (line)]] | wt | 8.69 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0567× (z -11.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 7.94 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +9.5) | — |
| [[H4 (line)]] | wt | 10.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0512× (z -9.5) |
| [[HCT15 (line)]] | alt | 19.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.47× (z +12.7) | — |
| [[HEC-1-A (line)]] | alt | 26.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.99× (z +13.9) | — |
| [[HS-578T (line)]] | alt | 7.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 4.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.92× (z +11.7) | — |
| [[LS 180 (line)]] | wt | 8.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 14.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.119× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 11.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.133× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 15.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.08× (z +13.1) | — |
| [[SNU-423 (line)]] | alt | 8.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -9.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 6.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.6× (z +9.8) | — |
| [[AN3 CA (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14390), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEKR1]] | +0.85 | +0.90 / +0.62 | both halves | 7e-06 |  |
| [[LINC02340]] | +0.83 | +0.88 / +0.66 | both halves | 7e-06 |  |
| [[PCNX4-DT]] | +0.81 | +0.86 / +0.58 | both halves | 8e-06 |  |
| [[KRCC1]] | +0.79 | +0.87 / +0.55 | both halves | 1e-05 |  |
| [[LINC00174]] | +0.79 | +0.87 / +0.53 | both halves | 1e-05 |  |
| [[AK9]] | +0.78 | +0.86 / +0.54 | both halves | 1e-05 |  |
| [[PPP3CB-AS1]] | +0.77 | +0.78 / +0.52 | both halves | 1e-05 |  |
| [[TMEM202-AS1]] | +0.76 | +0.83 / +0.47 | both halves | 2e-05 |  |
| [[TMEM232]] | +0.75 | +0.83 / +0.62 | both halves | 7e-06 |  |
| [[MZF1-AS1]] | +0.75 | +0.82 / +0.45 | both halves | 3e-05 |  |
| [[RAP2C-AS1]] | +0.75 | +0.85 / +0.49 | both halves | 1e-05 |  |
| [[LINC00667]] | +0.75 | +0.80 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACC1]] | -0.70 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[L2HGDH]] | -0.67 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[KLHL8]] | -0.67 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[ANKRD27]] | -0.66 | -0.74 / -0.31 | both halves | 2e-04 |  |
| [[GNA12]] | -0.66 | -0.73 / -0.28 | both halves | 3e-04 |  |
| [[LPCAT4]] | -0.66 | -0.74 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PDCL3P4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.851). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.4, 14.3); signed map (27.6, -11.0). **Vector** length 84.8, 20.3% of its response variance represented; |z| ≥ 3 in 1,220 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.3 | +24.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.9 | +12.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.0 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +16.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +8.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +4.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.3 | +3.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.9 | -8.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.4 | +7.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.0 | -5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | +7.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.7 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | +2.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.2 | -4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | PDCL3 pseudogene 4 |
| Locus type | pseudogene |
| Location | 3q12.3 — chr3:101,712,472-101,713,191 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44505](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44505) · Entrez [285359](https://www.ncbi.nlm.nih.gov/gene/285359) · Ensembl [ENSG00000244119](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244119)

## Data

Gene col 14390: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14390); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14390, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14390]; `tensor/DDL_lfc|DDL_z.npy` [14390]; `embed/gene_vectors.npy` [14390]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14390 or target_col == 14390). Every well: [[PDCL3P4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDCL3P4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
