---
symbol: "PABIR3"
type: "gene"
col: 7987
ensembl_id: "ENSG00000156500"
name: "PABIR family member 3"
location: "Xq26.3"
module: 69
arm: "+"
pooled_cpm: 20.65
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 25
n_dd_up_clean: 16
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# PABIR3

*PABIR family member 3* — Xq26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.37× (z +7.4, q 8e-11, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.400× (z -15.0, q 0e+00, down in 40 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[c-Kit-IN-1 (drug)]] 5 µM: 0.374× (z -8.3, q 3e-14, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYLD]] (+0.66, fdr 1e-05), [[RICTOR]] (+0.61, fdr 8e-05), [[HLA-B]] (+0.60, fdr 1e-05); moves opposite to [[POP1]] (-0.51, fdr 5e-05), [[POLR3H]] (-0.51, fdr 2e-05), [[AHCTF1]] (-0.50, fdr 5e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7987.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.4 | 8e-11 | 29/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +6.6 | 1e-08 | 30/45 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.31×** | +6.2 | 8e-08 | 22/45 (RKO, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +5.4 | 1e-05 | 21/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +5.2 | 2e-05 | 21/47 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.37×** | +5.1 | 2e-05 | 17/39 (HCT15, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +4.7 | 2e-04 | 20/46 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.7 | 2e-04 | 15/47 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.32×** | +4.6 | 3e-04 | 14/47 (SW480, hTERT-HPNE, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.30×** | +4.4 | 7e-04 | 16/47 (Hs 766T, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +4.3 | 7e-04 | 9/26 (SW1417, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +4.1 | 0.002 | 9/47 (SNU-1, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.002 | 16/47 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +4.0 | 0.003 | 16/47 (Panc 03.27, MIA PaCa-2, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.007 | 9/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.039 | 10/47 (Hs 766T, A549, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.039 | 12/46 (Hs 766T, C32, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.039 | 5/46 (BT-474, NCI-H2030, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.043 | 13/46 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7987.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.400×** | -15.0 | 0e+00 | 40/47 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.374×** | -8.3 | 3e-14 | 32/45 (SW480, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.379×** | -8.2 | 5e-14 | 31/47 (SW480, A498, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.397×** | -7.8 | 1e-12 | 33/44 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.661×** | -6.8 | 1e-09 | 24/46 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.462×** | -6.5 | 7e-09 | 25/44 (SW480, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.702×** | -5.8 | 5e-07 | 21/47 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.628×** | -5.5 | 4e-06 | 19/47 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.701×** | -5.4 | 4e-06 | 24/47 (SW480, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.730×** | -5.0 | 4e-05 | 20/42 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.557×** | -4.9 | 4e-05 | 20/38 (Panc 03.27, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.727×** | -4.9 | 5e-05 | 17/47 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.751×** | -4.7 | 1e-04 | 17/47 (SW480, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.823×** | -4.5 | 3e-04 | 20/46 (NCI-H1792, SNU-423, …) | top dose only | composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.621×** | -4.0 | 0.002 | 17/42 (SW480, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.784×** | -4.0 | 0.002 | 18/46 (Hs 766T, NCI-H661, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.711×** | -4.0 | 0.002 | 13/47 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.736×** | -3.6 | 0.010 | 8/47 (SW480, NCI-H1792, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.813×** | -3.4 | 0.019 | 10/46 (AN3 CA, NCI-H460, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7987. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 52.5 | 0 | 5 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.227× (z -15.1) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.367× (z -10.2) |
| [[A498 (line)]] | wt | 30.5 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.308× (z -9.9) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 20.2 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.230× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 27.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 27.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 19.2 | 0 | 1 | — | [[vincristine (drug)]] 0.5 µM 0.0743× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.125× (z -11.6) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -11.0) ⚠ cell-cycle shift, explains ~92% of this change |
| [[NCI-H2030 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0590× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[NCI-H460 (line)]] | wt | 19.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.160× (z -14.4) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -9.7) ⚠ cell-cycle shift, explains ~92% of this change |
| [[A-172 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7987), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYLD]] | +0.66 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[RICTOR]] | +0.61 | +0.37 / +0.64 | both halves | 8e-05 |  |
| [[HLA-B]] | +0.60 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[TMEM50A]] | +0.59 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[GBP4]] | +0.59 | +0.57 / +0.57 | both halves | 9e-06 |  |
| [[B2M]] | +0.58 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[NUB1]] | +0.58 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[SMIM14]] | +0.57 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[HLA-F]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[CHMP5]] | +0.57 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[HLA-E]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[HERC5]] | +0.56 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POP1]] | -0.51 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[POLR3H]] | -0.51 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[AHCTF1]] | -0.50 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[CCT4]] | -0.50 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[POLR1B]] | -0.48 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[CCT2]] | -0.48 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[EBPL]] | -0.47 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[GARNL3]] | -0.47 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[CCT3]] | -0.47 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[WDR3]] | -0.47 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[MRPL3]] | -0.47 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[POLR3B]] | -0.47 | -0.36 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PABIR3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers PABIR3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[IFIT3]] | B | IFIT3 activity lowers PABIR3's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 1.39× higher at baseline in the lines without IFIT3 | 0.095 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.5, 48.6); signed map (63.5, 26.5). **Vector** length 89.7, 18.7% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +7.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.4 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +5.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +4.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +4.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.9 | +2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +1.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.5 | -15.0 |
|  | [[EX229 (drug)]] 5 µM |  | -5.9 | -7.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.0 | -8.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.8 | -8.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.7 | -6.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.9 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | PABIR family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.3 — chrX:134,796,395-134,854,835 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RP3-473B4.1; previously FAM122C |
| Matched by | ensembl_id |

UniProt [Q6P4D5](https://www.uniprot.org/uniprotkb/Q6P4D5) carries no function annotation.

**Summary**, from NCBI Gene [159091](https://www.ncbi.nlm.nih.gov/gene/159091):

> Predicted to enable protein serine/threonine phosphatase inhibitor activity. Predicted to be involved in positive regulation of proteasomal ubiquitin-dependent protein catabolic process. Predicted to be active in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25202](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25202) · Entrez [159091](https://www.ncbi.nlm.nih.gov/gene/159091) · UniProt [Q6P4D5](https://www.uniprot.org/uniprotkb/Q6P4D5) · Ensembl [ENSG00000156500](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156500)

## Data

Gene col 7987: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7987); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7987, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7987]; `tensor/DDL_lfc|DDL_z.npy` [7987]; `embed/gene_vectors.npy` [7987]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7987 or target_col == 7987). Every well: [[PABIR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PABIR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
