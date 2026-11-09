---
symbol: "BDKRB2"
type: "gene"
col: 9644
ensembl_id: "ENSG00000168398"
name: "bradykinin receptor B2"
location: "14q32.2"
module: 14
arm: "+"
pooled_cpm: 15.1
n_lines_expressing: 32
n_dd_up: 21
n_dd_down: 47
n_dd_up_clean: 18
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 11
direction_downstream: 46
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# BDKRB2

*bradykinin receptor B2* — 14q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.45× (z +6.6, q 2e-08, up in 16 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 47 drug-doses (19 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.330× (z -19.5, q 0e+00, down in 28 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GBP2]] (+0.70, fdr 7e-06), [[BMF]] (+0.65, fdr 1e-05), [[ELF3]] (+0.62, fdr 1e-05); moves opposite to [[ZFYVE9]] (-0.52, fdr 3e-05), [[LAMB1]] (-0.51, fdr 5e-05), [[PHC2-AS1]] (-0.50, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[DUSP10]] → it (grade B ⚠); 46 go from it, the strongest it → [[DUSP10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9644.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +6.6 | 2e-08 | 16/30 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.55×** | +6.5 | 2e-08 | 15/30 (AsPC-1, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.66×** | +6.4 | 2e-08 | 17/30 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.62×** | +5.8 | 7e-07 | 18/29 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.57×** | +5.4 | 7e-06 | 15/29 (A549, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.32×** | +4.9 | 1e-04 | 13/30 (AsPC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.44×** | +4.6 | 4e-04 | 11/30 (SW480, J82, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.42×** | +4.3 | 0.001 | 11/30 (LS 180, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.41×** | +4.2 | 0.002 | 10/29 (LS 180, AsPC-1, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.41×** | +4.0 | 0.003 | 11/30 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.005 | 11/29 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.007 | 11/30 (J82, A-172, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.78×** | +3.8 | 0.007 | 9/30 (LoVo, AsPC-1, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.016 | 11/29 (hTERT-HPNE, A549, …) | rises with dose | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.019 | 11/30 (AsPC-1, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Alpelisib (drug)]] 5 µM |  | **1.69×** | +3.4 | 0.021 | 4/27 (LoVo, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.024 | 8/30 (LS 180, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 20 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 47 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9644.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.330×** | -19.5 | 0e+00 | 28/30 (HS-578T, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.425×** | -10.6 | 7e-24 | 25/30 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.452×** | -9.9 | 1e-20 | 22/29 (SHP-77, LS 180, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.477×** | -8.9 | 1e-16 | 23/27 (LS 180, COLO 205, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.500×** | -8.6 | 8e-16 | 21/30 (COLO 205, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.512×** | -8.3 | 1e-14 | 23/30 (RPMI-7951, HOP62, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.511×** | -7.9 | 3e-13 | 22/30 (SHP-77, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.557×** | -7.3 | 3e-11 | 20/30 (SHP-77, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.547×** | -7.2 | 4e-11 | 20/29 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.566×** | -7.1 | 1e-10 | 19/30 (SHP-77, LS 180, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.557×** | -7.0 | 1e-10 | 20/30 (HS-578T, AN3 CA, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.570×** | -7.0 | 1e-10 | 21/30 (RPMI-7951, HS-578T, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.594×** | -6.5 | 4e-09 | 16/30 (SHP-77, CHP-212, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **0.596×** | -6.4 | 5e-09 | 19/28 (CHP-212, AN3 CA, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.588×** | -6.3 | 9e-09 | 17/28 (RPMI-7951, SHP-77, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.711×** | -6.0 | 8e-08 | 19/30 (A498, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.761×** | -4.8 | 5e-05 | 19/30 (COLO 205, BT-474, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.687×** | -4.6 | 8e-05 | 14/30 (A549, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.705×** | -4.3 | 4e-04 | 15/30 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.713×** | -4.2 | 6e-04 | 12/30 (A549, A498, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.714×** | -4.2 | 6e-04 | 11/30 (A549, A498, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.724×** | -4.0 | 0.001 | 14/30 (A549, A498, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.726×** | -4.0 | 0.001 | 8/30 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.734×** | -3.8 | 0.002 | 14/30 (A549, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.66 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9644. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 109 | 0 | 14 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0763× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -19.8) |
| [[A549 (line)]] | wt | 32.5 | 0 | 11 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -14.2) |
| [[RPMI-7951 (line)]] | alt | 77.0 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0939× (z -20.7) |
| [[COLO 205 (line)]] | alt | 37.2 | 0 | 10 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -19.8) |
| [[LS 180 (line)]] | wt | 49.2 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0742× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -14.5) |
| [[CHP-212 (line)]] | wt | 98.6 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0663× (z -17.3) |
| [[HS-578T (line)]] | alt | 23.0 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0788× (z -22.2) |
| [[LoVo (line)]] | wt | 20.8 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -11.3) |
| [[HOP62 (line)]] | alt | 21.3 | 0 | 5 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0186× (z -23.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -13.5) |
| [[A498 (line)]] | wt | 34.7 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -13.1) |
| [[AN3 CA (line)]] | alt | 72.0 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -12.2) |
| [[A-172 (line)]] | wt | 11.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.20× (z +8.9) | — |
| [[J82 (line)]] | alt | 9.71 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.106× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -12.6) |
| [[SW 900 (line)]] | alt | 34.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0677× (z -16.7) |
| [[HCT15 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 4.26 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 12.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0982× (z -8.5) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 29.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -9.0) |
| [[A-427 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9644), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GBP2]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[BMF]] | +0.65 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[ELF3]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ATP8B1]] | +0.62 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ELF3-AS1]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[C15orf48]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[CGNL1]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[RIPK2]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[TMPRSS3]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[CFB]] | +0.55 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[SLC41A2]] | +0.55 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[ADGRG1]] | +0.55 | +0.46 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE9]] | -0.52 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[LAMB1]] | -0.51 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[PHC2-AS1]] | -0.50 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[BMS1P23]] | -0.50 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[CROCCP3-1]] | -0.47 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ANAPC1]] | -0.47 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[PDS5A]] | -0.47 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[SMYD2]] | -0.46 | -0.32 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 8, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUSP10]] | B | DUSP10 activity raises BDKRB2's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 4.82× lower at baseline in the lines without DUSP10 | 0.003 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[SLC44A4]] | B | SLC44A4 activity raises BDKRB2's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 1.88× lower at baseline in the lines without SLC44A4 | 0.023 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[RRAD]] | B | RRAD activity raises BDKRB2's level | lines that do not express RRAD (31) vs lines expressing it (19) | 2.31× lower at baseline in the lines without RRAD | 0.046 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[TRIM31]] | B | TRIM31 activity raises BDKRB2's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 1.94× lower at baseline in the lines without TRIM31 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers BDKRB2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[SLC40A1]] | B | SLC40A1 activity raises BDKRB2's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 1.90× lower at baseline in the lines without SLC40A1 | 0.079 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[TOP2A]] | B | TOP2A activity raises BDKRB2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.4% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BMP2]] | B | BMP2 activity raises BDKRB2's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 2.46× lower at baseline in the lines without BMP2 | 0.088 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[NOD2]] | C | NOD2 activity raises BDKRB2's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 4.38× lower at baseline in the lines without NOD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2; co-absent with the target |
| [[ACKR3]] | C | ACKR3 activity raises BDKRB2's level | lines that do not express ACKR3 (30) vs lines expressing it (20) | 2.87× lower at baseline in the lines without ACKR3 | 0.054 | ⚠ within organs, on part of the lines; also absent: IGFN1, ITGA11, NCAM1; co-absent with the target |
| [[RASSF6]] | C | RASSF6 activity raises BDKRB2's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.30× lower at baseline in the lines without RASSF6 | 0.055 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6; co-absent with the target |

### Downstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 37, C 9. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUSP10]] | B | BDKRB2 activity raises DUSP10's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 3.45× lower at baseline in the lines without BDKRB2 | 0.002 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[BMF]] | B | BDKRB2 activity raises BMF's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 2.22× lower at baseline in the lines without BDKRB2 | 0.010 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[CROCCP3-1]] | B | BDKRB2 activity weakens CROCCP3-1's drug response | lines that do not express BDKRB2 (18) vs lines expressing it (29) | the lines without BDKRB2 respond 1.54× as strongly (z diff -1.80); strongest at Harringtonine 0.5 µM: 0.37x vs 0.64x (z diff -2.8) | 0.014 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003; target measured in part of the lines; artifact flags |
| [[CROCCP3-1]] | B | BDKRB2 activity lowers CROCCP3-1's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 1.66× higher at baseline in the lines without BDKRB2 | 0.018 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[BCL3]] | B | BDKRB2 activity raises BCL3's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 1.84× lower at baseline in the lines without BDKRB2 | 0.019 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[CXXC5]] | B | BDKRB2 activity raises CXXC5's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 3.37× lower at baseline in the lines without BDKRB2 | 0.022 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[LRIG1]] | B | BDKRB2 activity raises LRIG1's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 3.02× lower at baseline in the lines without BDKRB2 | 0.023 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[THEMIS2]] | B | BDKRB2 activity raises THEMIS2's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 1.95× lower at baseline in the lines without BDKRB2 | 0.023 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[RRAD]] | B | BDKRB2 activity raises RRAD's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 2.22× lower at baseline in the lines without BDKRB2 | 0.028 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[SLC4A4]] | B | BDKRB2 activity raises SLC4A4's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 2.18× lower at baseline in the lines without BDKRB2 | 0.042 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[ATP8B1]] | B | BDKRB2 activity raises ATP8B1's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 3.15× lower at baseline in the lines without BDKRB2 | 0.044 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[GBP2]] | B | BDKRB2 activity raises GBP2's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 2.80× lower at baseline in the lines without BDKRB2 | 0.045 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.553). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.6, -0.7); signed map (47.0, 9.5). **Vector** length 95.1, 24.0% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.9 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | +5.9 | -6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +5.7 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | +5.1 | -5.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +6.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +5.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.8 | +4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +4.2 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -3.8 | -2.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.6 | -3.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.3 | -3.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.1 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -3.0 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | bradykinin receptor B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.2 — chr14:96,204,679-96,244,166 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BK-2 |
| Gene groups (HGNC) | Bradykinin receptors |
| Hallmark sets | MYOGENESIS |
| Reactome | 7 pathways, smallest: Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P30411](https://www.uniprot.org/uniprotkb/P30411) (B2 bradykinin receptor):

> Receptor for bradykinin. It is associated with G proteins that activate a phosphatidylinositol-calcium second messenger system.

**Summary**, from NCBI Gene [624](https://www.ncbi.nlm.nih.gov/gene/624):

> This gene encodes a receptor for bradykinin. The 9 aa bradykinin peptide elicits many responses including vasodilation, edema, smooth muscle spasm and pain fiber stimulation. Bradykinin is released upon activation by pathophysiologic conditions such as trauma and inflammation, and binds to its kinin receptors, B1 and B2. The B2 receptor associates with G proteins that stimulate a phosphatidylinositol-calcium second messenger system. [provided by RefSeq, Apr 2020]

**Accessions** — [HGNC:1030](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1030) · Entrez [624](https://www.ncbi.nlm.nih.gov/gene/624) · UniProt [P30411](https://www.uniprot.org/uniprotkb/P30411) · Ensembl [ENSG00000168398](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168398)

## Data

Gene col 9644: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9644); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9644, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9644]; `tensor/DDL_lfc|DDL_z.npy` [9644]; `embed/gene_vectors.npy` [9644]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9644 or target_col == 9644). Every well: [[BDKRB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BDKRB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
