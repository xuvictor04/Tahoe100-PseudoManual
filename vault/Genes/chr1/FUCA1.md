---
symbol: "FUCA1"
type: "gene"
col: 11007
ensembl_id: "ENSG00000179163"
name: "alpha-L-fucosidase 1"
location: "1p36.11"
module: 50
arm: "+"
pooled_cpm: 13.58
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 19
n_dd_up_clean: 20
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# FUCA1

*alpha-L-fucosidase 1* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.88× (z +26.5, q 0e+00, up in 42 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.522× (z -9.0, q 1e-16, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6AP2]] (+0.69, fdr 1e-05), [[MOSPD3]] (+0.66, fdr 1e-05), [[PIGS]] (+0.64, fdr 7e-06); moves opposite to [[DPH5]] (-0.59, fdr 1e-05), [[CDKL1]] (-0.58, fdr 1e-05), [[JPX]] (-0.58, fdr 5e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11007.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.88×** | +26.5 | 0e+00 | 42/43 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.18×** | +16.0 | 0e+00 | 44/47 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.83×** | +14.4 | 1e-44 | 42/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.45×** | +12.4 | 4e-33 | 39/46 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +8.4 | 8e-15 | 29/41 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.71×** | +7.4 | 9e-12 | 32/47 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +7.2 | 4e-11 | 26/43 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +7.2 | 5e-11 | 32/47 (HOP62, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.66×** | +6.8 | 8e-10 | 12/22 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +6.8 | 8e-10 | 23/47 (SW1417, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.54×** | +6.0 | 1e-07 | 18/35 (HEC-1-A, A549, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +6.0 | 1e-07 | 20/46 (RKO, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +5.2 | 8e-06 | 20/43 (NCI-H2030, SW1417, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.9 | 4e-05 | 7/47 (NCI-H2030, LS 180, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.52×** | +4.1 | 0.001 | 6/44 (PANC-1, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.001 | 15/46 (CFPAC-1, KATO III, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.94×** | +4.1 | 0.002 | 8/45 (PANC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.85×** | +3.8 | 0.004 | 11/44 (SW1417, H4, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11007.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.522×** | -9.0 | 1e-16 | 28/46 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.536×** | -8.6 | 2e-15 | 29/46 (SW 900, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.585×** | -7.2 | 2e-10 | 28/46 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.600×** | -7.1 | 2e-10 | 26/46 (CFPAC-1, NCI-H460, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.620×** | -6.6 | 4e-09 | 29/45 (SW 900, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.632×** | -6.3 | 2e-08 | 22/45 (Hs 766T, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.741×** | -5.9 | 3e-07 | 20/43 (NCI-H2030, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.565×** | -5.5 | 3e-06 | 22/42 (HCT15, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.643×** | -5.2 | 2e-05 | 22/45 (SW1417, LS 180, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.701×** | -4.9 | 5e-05 | 24/45 (HT-29, AN3 CA, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.717×** | -4.6 | 2e-04 | 20/47 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.748×** | -4.0 | 0.003 | 16/46 (PANC-1, SW 900, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.753×** | -3.9 | 0.004 | 16/45 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.757×** | -3.9 | 0.005 | 16/46 (LS 180, SW 900, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.757×** | -3.6 | 0.013 | 20/42 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11007. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 10.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +10.5) | — |
| [[NCI-H2347 (line)]] | alt | 32.4 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.8) | [[Harringtonine (drug)]] 0.5 µM 0.325× (z -10.6) |
| [[A498 (line)]] | wt | 12.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +10.0) | [[Harringtonine (drug)]] 0.5 µM 0.205× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 7.04 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +9.2) | [[Harringtonine (drug)]] 0.05 µM 0.0721× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 39.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +12.4) | [[Harringtonine (drug)]] 0.05 µM 0.287× (z -8.7) |
| [[LoVo (line)]] | wt | 13.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.29× (z +16.3) | — |
| [[LS 180 (line)]] | wt | 24.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +14.3) | [[Ixazomib citrate (drug)]] 5 µM 0.267× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 18.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 6.93 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +10.4) | [[Harringtonine (drug)]] 0.05 µM 0.208× (z -8.6) |
| [[SW1417 (line)]] | alt | 25.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +12.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.318× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~42% of this change |
| [[A549 (line)]] | wt | 6.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.69× (z +12.8) | — |
| [[C-33 A (line)]] | alt | 14.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.48× (z +10.9) | — |
| [[H4 (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0750× (z -9.1) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 15.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.15× (z +16.7) | — |
| [[HepG2_C3A (line)]] | wt | 29.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +11.7) | — |
| [[HOP62 (line)]] | alt | 12.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +10.9) | — |
| [[HT-29 (line)]] | alt | 19.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +12.7) | — |
| [[KATO III (line)]] | alt | 25.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.17× (z +15.4) | — |
| [[NCI-H1573 (line)]] | alt | 8.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 9.57 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.157× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +10.8) | — |
| [[RKO (line)]] | wt | 6.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.32× (z +10.9) | — |
| [[SHP-77 (line)]] | alt | 6.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.67× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 13.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -8.7) |
| [[SW 900 (line)]] | alt | 37.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.228× (z -8.9) |
| [[SW480 (line)]] | alt | 14.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +15.8) | — |
| [[A-172 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11007), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6AP2]] | +0.69 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.66 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[PIGS]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.63 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[SMAP2]] | +0.62 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[GM2A]] | +0.61 | +0.52 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY; STRING 420 |
| [[NDUFA2]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[TMED4]] | +0.61 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[TRAPPC1]] | +0.60 | +0.42 / +0.60 | both halves | 4e-05 | pathway: Asparagine N-linked glycosylation |
| [[FAM234A]] | +0.59 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[BSG]] | +0.58 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[APAF1]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPH5]] | -0.59 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[CDKL1]] | -0.58 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[JPX]] | -0.58 | -0.40 / -0.61 | both halves | 5e-05 |  |
| [[ALOX12P2-1]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ATP9B]] | -0.58 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[ANKLE2]] | -0.57 | -0.37 / -0.64 | both halves | 7e-05 |  |
| [[RAD23A]] | -0.57 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[EIF3J]] | -0.56 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[CHMP6]] | -0.56 | -0.37 / -0.61 | both halves | 8e-05 |  |
| [[TIAM2]] | -0.56 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[ANAPC7]] | -0.55 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[GPATCH4]] | -0.55 | -0.47 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FUCA1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.519). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.0, -20.0); signed map (-35.5, 14.7). **Vector** length 85.4, 18.5% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +26.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +8.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.2 | +3.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +6.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +7.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | -0.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +6.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +4.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.9 | -4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.8 | -9.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.1 | -8.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -7.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | alpha-L-fucosidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:23,845,077-23,868,290 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Alpha-L-fucosidases |
| Hallmark sets | KRAS_SIGNALING_UP, EPITHELIAL_MESENCHYMAL_TRANSITION, P53_PATHWAY |
| Reactome | 6 pathways, smallest: Reactions specific to the complex N-glycan synthesis pathway; N-glycan antennae elongation in the medial/trans-Golgi; Transport to the Golgi and subsequent modification |
| Matched by | ensembl_id |

**Function**, from UniProt [P04066](https://www.uniprot.org/uniprotkb/P04066) (Tissue alpha-L-fucosidase):

> Alpha-L-fucosidase is responsible for hydrolyzing the alpha-1,6-linked fucose joined to the reducing-end N-acetylglucosamine of the carbohydrate moieties of glycoproteins.

**Summary**, from NCBI Gene [2517](https://www.ncbi.nlm.nih.gov/gene/2517):

> The protein encoded by this gene is a lysosomal enzyme involved in the degradation of fucose-containing glycoproteins and glycolipids. Mutations in this gene are associated with fucosidosis (FUCA1D), which is an autosomal recessive lysosomal storage disease. A pseudogene of this locus is present on chr 2.[provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:4006](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4006) · Entrez [2517](https://www.ncbi.nlm.nih.gov/gene/2517) · UniProt [P04066](https://www.uniprot.org/uniprotkb/P04066) · Ensembl [ENSG00000179163](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179163)

## Data

Gene col 11007: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11007); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11007, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11007]; `tensor/DDL_lfc|DDL_z.npy` [11007]; `embed/gene_vectors.npy` [11007]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11007 or target_col == 11007). Every well: [[FUCA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FUCA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
