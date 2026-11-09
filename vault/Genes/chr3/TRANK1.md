---
symbol: "TRANK1"
type: "gene"
col: 9582
ensembl_id: "ENSG00000168016"
name: "tetratricopeptide repeat and ankyrin repeat containing 1"
location: "3p22.2"
module: 70
arm: "+"
pooled_cpm: 26.37
n_lines_expressing: 43
n_dd_up: 21
n_dd_down: 51
n_dd_up_clean: 21
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 63
direction_downstream: 27
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# TRANK1

*tetratricopeptide repeat and ankyrin repeat containing 1* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 2.38× (z +8.2, q 1e-13, up in 33 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 51 drug-doses (20 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.259× (z -13.2, q 4e-37, down in 40 of 41 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Tofacitinib (drug)]] 5 µM: 0.510× (z -9.3, q 5e-18, down in 27 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM22]] (+0.88, fdr 7e-06), [[IFIT2]] (+0.88, fdr 7e-06), [[IFIT3]] (+0.88, fdr 7e-06).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 63 arrows point to it, the strongest [[RSAD2]] → it (grade B ⚠); 27 go from it, the strongest it → [[CASP10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, none with an alert; shown: the 15 strongest. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9582.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **2.38×** | +8.2 | 1e-13 | 33/39 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.64×** | +6.1 | 3e-07 | 28/41 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.78×** | +5.7 | 2e-06 | 28/40 (AsPC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.76×** | +5.6 | 3e-06 | 28/41 (AsPC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.76×** | +5.4 | 9e-06 | 23/40 (AsPC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.42×** | +4.8 | 1e-04 | 24/41 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.61×** | +4.7 | 2e-04 | 23/41 (LoVo, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +4.7 | 2e-04 | 23/40 (NCI-H2347, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.49×** | +4.7 | 2e-04 | 26/40 (AsPC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.39×** | +4.5 | 3e-04 | 22/41 (CFPAC-1, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.56×** | +4.4 | 6e-04 | 19/41 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.61×** | +4.4 | 6e-04 | 24/41 (CFPAC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.50×** | +4.0 | 0.003 | 21/41 (RKO, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.52×** | +3.9 | 0.003 | 19/39 (CFPAC-1, LoVo, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **2.04×** | +3.7 | 0.008 | 23/39 (LoVo, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 20 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 51 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9582.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.259×** | -13.2 | 4e-37 | 40/41 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.510×** | -9.3 | 5e-18 | 27/41 (MIA PaCa-2, RPMI-7951, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.575×** | -7.6 | 5e-12 | 28/41 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.586×** | -7.3 | 3e-11 | 31/41 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.474×** | -7.3 | 4e-11 | 28/38 (A-172, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.481×** | -7.1 | 9e-11 | 26/39 (RPMI-7951, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.474×** | -7.0 | 2e-10 | 27/37 (SNU-423, A549, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.495×** | -6.8 | 5e-10 | 28/41 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.499×** | -6.8 | 8e-10 | 27/41 (MIA PaCa-2, COLO 205, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.503×** | -6.7 | 1e-09 | 26/41 (MIA PaCa-2, COLO 205, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.509×** | -6.6 | 2e-09 | 26/40 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.277×** | -6.6 | 2e-09 | 32/39 (COLO 205, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.515×** | -6.1 | 4e-08 | 26/38 (MIA PaCa-2, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.305×** | -6.1 | 5e-08 | 31/38 (RKO, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.539×** | -6.0 | 6e-08 | 26/41 (COLO 205, A-172, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.542×** | -6.0 | 8e-08 | 26/41 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.568×** | -5.5 | 1e-06 | 26/40 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.569×** | -5.5 | 1e-06 | 24/41 (RPMI-7951, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.603×** | -4.7 | 5e-05 | 23/39 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.644×** | -4.3 | 4e-04 | 21/40 (NCI-H23, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9582. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 46.2 | 0 | 13 (5 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.125× (z -14.9) |
| [[NCI-H2347 (line)]] | alt | 49.6 | 1 | 7 (4 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.62× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.228× (z -10.1) |
| [[A549 (line)]] | wt | 85.0 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -14.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.206× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 91.4 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.332× (z -10.6) |
| [[SNU-423 (line)]] | alt | 58.5 | 0 | 7 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0177× (z -21.0) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.170× (z -9.6) |
| [[A-172 (line)]] | wt | 61.1 | 0 | 6 (4 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.144× (z -11.6) |
| [[LoVo (line)]] | wt | 34.6 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.46× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0934× (z -14.6) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.209× (z -9.1) |
| [[COLO 205 (line)]] | alt | 55.0 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 40.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 25.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.139× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 33.6 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.166× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 25.5 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.102× (z -15.9) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 50.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0885× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.194× (z -10.6) |
| [[RKO (line)]] | wt | 19.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -10.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Peretinoin (drug)]] 5 µM 0.105× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 56.8 | 0 | 3 (3 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0637× (z -9.6) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 33.6 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.158× (z -9.4) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 26.4 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.238× (z -9.2) |
| [[C32 (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[HT-29 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.160× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[J82 (line)]] | alt | 18.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LS 180 (line)]] | wt | 25.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[NCI-H1573 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[NCI-H2030 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0966× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[NCI-H23 (line)]] | alt | 30.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.174× (z -8.5) |
| [[PANC-1 (line)]] | alt | 8.41 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.182× (z -9.7) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 27.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0994× (z -14.5) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 4.39 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.33 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.71 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.98 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9582), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM22]] | +0.88 | +0.86 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[IFIT2]] | +0.88 | +0.87 / +0.86 | both halves | 7e-06 | same gene group |
| [[IFIT3]] | +0.88 | +0.88 / +0.85 | both halves | 7e-06 | same gene group |
| [[PARP14]] | +0.87 | +0.84 / +0.86 | both halves | 7e-06 |  |
| [[IFIT1]] | +0.87 | +0.86 / +0.87 | both halves | 7e-06 | same gene group |
| [[IFI35]] | +0.87 | +0.85 / +0.84 | both halves | 7e-06 |  |
| [[HERC5]] | +0.86 | +0.85 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[TMEM140]] | +0.86 | +0.80 / +0.86 | both halves | 7e-06 | STRING 400 |
| [[SAMD9L]] | +0.86 | +0.81 / +0.86 | both halves | 7e-06 |  |
| [[PARP9]] | +0.86 | +0.85 / +0.83 | both halves | 7e-06 |  |
| [[OAS1]] | +0.86 | +0.84 / +0.86 | both halves | 7e-06 |  |
| [[NMI]] | +0.86 | +0.80 / +0.87 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*63 arrows, 63 of them with an alert ⚠; grade A 0, B 42, C 21. Shown: the 12 strongest; 51 more arrows (51 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RSAD2]] | B | RSAD2 activity raises TRANK1's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.89× lower at baseline in the lines without RSAD2 | 0.002 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[OAS1]] | B | OAS1 activity raises TRANK1's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.60× lower at baseline in the lines without OAS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[CD5L]] | B | CD5L activity raises TRANK1's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.52× lower at baseline in the lines without CD5L | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[TRIM22]] | B | TRIM22 activity raises TRANK1's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.75× lower at baseline in the lines without TRIM22 | 0.008 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[CASP10]] | B | CASP10 activity raises TRANK1's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.25× lower at baseline in the lines without CASP10 | 0.009 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[PLAAT4]] | B | PLAAT4 activity raises TRANK1's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.04× lower at baseline in the lines without PLAAT4 | 0.009 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[HERC6]] | B | HERC6 activity raises TRANK1's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 2.94× lower at baseline in the lines without HERC6 | 0.010 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[SAMD9L]] | B | SAMD9L activity raises TRANK1's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.28× lower at baseline in the lines without SAMD9L | 0.010 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[OAS3]] | B | OAS3 activity raises TRANK1's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 2.87× lower at baseline in the lines without OAS3 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[APOL6]] | B | APOL6 activity raises TRANK1's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 3.14× lower at baseline in the lines without APOL6 | 0.012 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[IFI44]] | B | IFI44 activity raises TRANK1's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.51× lower at baseline in the lines without IFI44 | 0.012 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[OAS2]] | B | OAS2 activity raises TRANK1's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.22× lower at baseline in the lines without OAS2 | 0.013 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 27, C 0. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASP10]] | B | TRANK1 activity raises CASP10's level | lines that do not express TRANK1 (7) vs lines expressing it (43) | 3.92× lower at baseline in the lines without TRANK1 | 0.012 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TMEM140]] | B | TRANK1 activity raises TMEM140's level | lines that do not express TRANK1 (7) vs lines expressing it (43) | 2.40× lower at baseline in the lines without TRANK1 | 0.013 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[IFIT3]] | B | TRANK1 activity raises IFIT3's level | lines that do not express TRANK1 (7) vs lines expressing it (43) | 3.26× lower at baseline in the lines without TRANK1 | 0.014 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[IFIT1]] | B | TRANK1 activity raises IFIT1's level | lines that do not express TRANK1 (7) vs lines expressing it (43) | 2.44× lower at baseline in the lines without TRANK1 | 0.015 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[OAS1]] | B | TRANK1 activity raises OAS1's level | lines that do not express TRANK1 (7) vs lines expressing it (43) | 3.48× lower at baseline in the lines without TRANK1 | 0.015 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[DDX60]] | B | TRANK1 activity raises DDX60's level | lines that do not express TRANK1 (7) vs lines expressing it (43) | 2.97× lower at baseline in the lines without TRANK1 | 0.019 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TRIM38]] | B | TRANK1 activity raises TRIM38's level | lines that do not express TRANK1 (7) vs lines expressing it (43) | 2.62× lower at baseline in the lines without TRANK1 | 0.024 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NCOA7]] | B | TRANK1 activity raises NCOA7's level | lines that do not express TRANK1 (7) vs lines expressing it (43) | 2.01× lower at baseline in the lines without TRANK1 | 0.026 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MYD88]] | B | TRANK1 activity raises MYD88's level | lines that do not express TRANK1 (7) vs lines expressing it (43) | 1.91× lower at baseline in the lines without TRANK1 | 0.028 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[IFITM1]] | B | TRANK1 activity raises IFITM1's level | lines that do not express TRANK1 (7) vs lines expressing it (43) | 4.36× lower at baseline in the lines without TRANK1 | 0.033 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[IFI6]] | B | TRANK1 activity raises IFI6's level | lines that do not express TRANK1 (7) vs lines expressing it (43) | 2.36× lower at baseline in the lines without TRANK1 | 0.034 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[DDX60L]] | B | TRANK1 activity raises DDX60L's level | lines that do not express TRANK1 (7) vs lines expressing it (43) | 2.89× lower at baseline in the lines without TRANK1 | 0.037 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.876). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.9, 53.0); signed map (63.0, 31.0). **Vector** length 133, 43.9% of its response variance represented; |z| ≥ 3 in 1,493 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.63 to 25); *interferon alpha response* (hallmark, mean cos +0.62 to 19); *Antigen processing-Cross presentation* (reactome, mean cos +0.64 to 14).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.0 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.5 | +1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.5 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +5.0 | +3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.5 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.3 | +5.4 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -8.0 | -9.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -7.2 | -7.6 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -7.0 | -7.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.5 | -13.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -6.4 | -6.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -6.0 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat and ankyrin repeat containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.2 — chr3:36,826,819-36,945,057 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LBA1, KIAA0342 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

UniProt [O15050](https://www.uniprot.org/uniprotkb/O15050) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:29011](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29011) · Entrez [9881](https://www.ncbi.nlm.nih.gov/gene/9881) · UniProt [O15050](https://www.uniprot.org/uniprotkb/O15050) · Ensembl [ENSG00000168016](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168016)

## Data

Gene col 9582: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9582); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9582, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9582]; `tensor/DDL_lfc|DDL_z.npy` [9582]; `embed/gene_vectors.npy` [9582]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9582 or target_col == 9582). Every well: [[TRANK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRANK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
