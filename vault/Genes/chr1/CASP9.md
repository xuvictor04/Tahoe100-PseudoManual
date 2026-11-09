---
symbol: "CASP9"
type: "gene"
col: 5389
ensembl_id: "ENSG00000132906"
name: "caspase 9"
location: "1p36.21"
module: 1
arm: "-"
pooled_cpm: 15.53
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 28
n_dd_up_clean: 6
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# CASP9

*caspase 9* — 1p36.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.05× (z +12.6, q 1e-33, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.523× (z -11.4, q 4e-27, down in 28 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.542× (z -10.7, q 2e-24, down in 29 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAAF3]] (+0.69, fdr 1e-05), [[RASSF7]] (+0.63, fdr 6e-05), [[RHPN2]] (+0.63, fdr 5e-05); moves opposite to [[METTL8]] (-0.62, fdr 1e-05), [[UTP20]] (-0.61, fdr 2e-05), [[DNAJC11]] (-0.60, fdr 3e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5389.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.05×** | +12.6 | 1e-33 | 35/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.96×** | +11.8 | 1e-29 | 38/47 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.80×** | +10.4 | 7e-23 | 32/46 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +6.4 | 3e-08 | 21/47 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.3 | 0.002 | 15/47 (HOP62, SK-MEL-2, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.007 | 5/46 (KATO III, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.046 | 9/47 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.12 | 6/46 (NCI-H2030, C32, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 14 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5389.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.523×** | -11.4 | 4e-27 | 28/36 (PANC-1, NCI-H2030, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.542×** | -10.7 | 2e-24 | 29/44 (LoVo, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.610×** | -8.0 | 2e-13 | 22/32 (SW1417, NCI-H2030, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.664×** | -7.2 | 1e-10 | 23/47 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.649×** | -7.0 | 2e-10 | 18/24 (HS-578T, RPMI-7951, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.683×** | -6.7 | 2e-09 | 23/45 (SW 900, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.484×** | -6.6 | 2e-09 | 26/47 (HS-578T, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.671×** | -6.5 | 5e-09 | 19/41 (RPMI-7951, A498, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.693×** | -6.4 | 8e-09 | 20/46 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.788×** | -5.9 | 2e-07 | 23/46 (NCI-H1792, LoVo, …) | two highest doses | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.716×** | -5.8 | 3e-07 | 18/46 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.719×** | -5.8 | 3e-07 | 17/46 (SW 900, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.719×** | -5.8 | 3e-07 | 18/46 (HS-578T, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.730×** | -5.5 | 1e-06 | 20/45 (LoVo, PANC-1, …) | two highest doses | cell-cycle shift (explains ~16% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.573×** | -5.1 | 1e-05 | 17/39 (NCI-H1573, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.597×** | -4.7 | 8e-05 | 13/43 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.780×** | -4.3 | 4e-04 | 15/46 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.854× | -3.9 | 0.003 | 14/47 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.809×** | -3.7 | 0.005 | 18/46 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.818×** | -3.5 | 0.011 | 7/46 (HT-29, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.819×** | -3.5 | 0.011 | 15/45 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.810×** | -3.4 | 0.014 | 7/47 (HT-29, NCI-H1573, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.813×** | -3.4 | 0.016 | 12/46 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.715×** | -3.1 | 0.044 | 11/47 (NCI-H460, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.722×** | -3.0 | 0.057 | 7/44 (NCI-H1573, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.729×** | -2.9 | 0.073 | 9/45 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5389. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 24.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.252× (z -8.9) |
| [[LoVo (line)]] | wt | 24.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 28.5 | 0 | 3 (3 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0467× (z -11.6) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 21.9 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.01× (z +10.9) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.86× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 17.1 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -10.4) |
| [[HT-29 (line)]] | alt | 18.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[KATO III (line)]] | alt | 9.46 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 22.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -16.5) ⚠ cell-cycle shift, explains ~56% of this change |
| [[NCI-H2030 (line)]] | alt | 14.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 13.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[RPMI-7951 (line)]] | alt | 15.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0800× (z -12.3) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[A498 (line)]] | wt | 8.24 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.141× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[A549 (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0537× (z -9.7) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 15.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.256× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HCT15 (line)]] | alt | 18.3 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0960× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HepG2_C3A (line)]] | wt | 30.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.216× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[J82 (line)]] | alt | 9.61 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -10.6) |
| [[SNU-1 (line)]] | wt | 9.35 | 0 | 1 | — | [[Terfenadine (drug)]] 0.5 µM 0.0743× (z -8.8) |
| [[SNU-423 (line)]] | alt | 13.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.214× (z -8.5) |
| [[SW1417 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.81 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5389), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF3]] | +0.69 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[RASSF7]] | +0.63 | +0.63 / +0.39 | both halves | 6e-05 |  |
| [[RHPN2]] | +0.63 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[FBXO33]] | +0.62 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[PTPRH]] | +0.62 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[CARD19]] | +0.61 | +0.54 / +0.48 | both halves | 2e-05 | same gene group |
| [[CARHSP1]] | +0.61 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[DOK4]] | +0.60 | +0.59 / +0.23 | both halves | 5e-04 |  |
| [[TNNI3]] | +0.59 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[FA2H]] | +0.59 | +0.56 / +0.39 | both halves | 5e-05 |  |
| [[TMEM256]] | +0.59 | +0.50 / +0.34 | both halves | 1e-04 |  |
| [[CDKN2D]] | +0.59 | +0.43 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL8]] | -0.62 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[UTP20]] | -0.61 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[DNAJC11]] | -0.60 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[USP7]] | -0.60 | -0.42 / -0.38 | both halves | 6e-05 | pathway: Intracellular signaling by second messengers |
| [[PYGO1]] | -0.60 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[ABCE1]] | -0.59 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ZNF507]] | -0.59 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[ALG8]] | -0.59 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[PRDM5]] | -0.58 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[SNX5]] | -0.58 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[PRRC2B]] | -0.58 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[MAPKAPK5]] | -0.57 | -0.44 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CASP9's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FA2H]] | B | FA2H activity raises CASP9's level | lines that do not express FA2H (27) vs lines expressing it (23) | 1.38× lower at baseline in the lines without FA2H | 0.092 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.521). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (5.3, -3.7); signed map (-30.0, 18.4). **Vector** length 76.9, 13.7% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +11.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.7 | +12.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.2 | +10.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +3.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +4.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.3 | +1.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +1.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.3 | +1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -10.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.6 | -4.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.4 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -4.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | caspase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.21 — chr1:15,490,832-15,526,534 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MCH6, ICE-LAP6, APAF-3, PPP1R56 |
| Gene groups (HGNC) | Caspases; Protein phosphatase 1 regulatory subunits; Caspase recruitment domain containing; Apoptosome |
| Hallmark sets | COAGULATION, APOPTOSIS, COMPLEMENT |
| Reactome | 22 pathways, smallest: Activation of caspases through apoptosome-mediated cleavage; SMAC (DIABLO) binds to IAPs; SMAC(DIABLO)-mediated dissociation of IAP:caspase complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [P55211](https://www.uniprot.org/uniprotkb/P55211) (Caspase-9):

> Involved in the activation cascade of caspases responsible for apoptosis execution. Binding of caspase-9 to Apaf-1 leads to activation of the protease which then cleaves and activates effector caspases caspase-3 (CASP3) or caspase-7 (CASP7). Promotes DNA damage-induced apoptosis in a ABL1/c-Abl-dependent manner. Proteolytically cleaves poly(ADP-ribose) polymerase (PARP). Cleaves BIRC6 following inhibition of BIRC6-caspase binding by DIABLO/SMAC.; [Isoform 2]: Lacks activity is an …

**Summary**, from NCBI Gene [842](https://www.ncbi.nlm.nih.gov/gene/842):

> This gene encodes a member of the cysteine-aspartic acid protease (caspase) family. Sequential activation of caspases plays a central role in the execution-phase of cell apoptosis. Caspases exist as inactive proenzymes which undergo proteolytic processing at conserved aspartic residues to produce two subunits, large and small, that dimerize to form the active enzyme. This protein can undergo autoproteolytic processing and activation by the apoptosome, a protein complex of cytochrome c and the …

**Accessions** — [HGNC:1511](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1511) · Entrez [842](https://www.ncbi.nlm.nih.gov/gene/842) · UniProt [P55211](https://www.uniprot.org/uniprotkb/P55211) · Ensembl [ENSG00000132906](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132906)

## Data

Gene col 5389: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5389); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5389, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5389]; `tensor/DDL_lfc|DDL_z.npy` [5389]; `embed/gene_vectors.npy` [5389]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5389 or target_col == 5389). Every well: [[CASP9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASP9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
