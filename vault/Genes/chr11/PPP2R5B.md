---
symbol: "PPP2R5B"
type: "gene"
col: 906
ensembl_id: "ENSG00000068971"
name: "protein phosphatase 2 regulatory subunit B'beta"
location: "11q13.1"
module: 180
arm: "+"
pooled_cpm: 17.87
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 22
n_dd_up_clean: 17
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/180"]
generated_by: "tahoemap"
---

# PPP2R5B

*protein phosphatase 2 regulatory subunit B'beta* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.50× (z +7.0, q 1e-09, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.486× (z -8.5, q 2e-14, down in 32 of 45 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.715× (z -5.8, q 1e-06, down in 26 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NGLY1]] (+0.72, fdr 7e-06), [[ENO2]] (+0.72, fdr 7e-06), [[FBXO42]] (+0.68, fdr 7e-06); moves opposite to [[UTP20]] (-0.64, fdr 1e-05), [[SNX5]] (-0.61, fdr 1e-05), [[ILF3]] (-0.61, fdr 1e-05).
> It is in [[Module 180]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[RALGDS]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 906.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.50×** | +7.0 | 1e-09 | 33/48 (LS 180, Panc 03.27, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.55×** | +5.3 | 3e-05 | 29/47 (LoVo, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +5.1 | 4e-05 | 24/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +5.1 | 4e-05 | 26/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.42×** | +4.3 | 0.002 | 21/46 (LS 180, LoVo, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.91×** | +4.1 | 0.004 | 19/45 (CFPAC-1, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.004 | 21/47 (LS 180, COLO 205, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.57×** | +3.9 | 0.006 | 19/48 (SW 900, SNU-423, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.011 | 20/46 (NCI-H2030, RKO, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.011 | 21/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 5 µM |  | **1.76×** | +3.6 | 0.016 | 15/43 (CFPAC-1, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.028 | 17/47 (NCI-H2030, RKO, …) | rises with dose | low cells (technical?) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.051 | 14/47 (SW 900, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.051 | 18/47 (COLO 205, LS 180, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.20× | +3.1 | 0.062 | 13/48 (KATO III, Hs 766T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.072 | 16/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.087 | 5/48 (HS-578T, NCI-H460, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 906.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.486×** | -8.5 | 2e-14 | 32/45 (SNU-423, BT-474, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.854× | -7.0 | 8e-10 | 18/48 (NCI-H2030, SNU-423, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.715×** | -5.8 | 1e-06 | 26/45 (SNU-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.649×** | -5.1 | 5e-05 | 26/46 (HS-578T, RKO, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.650×** | -5.1 | 5e-05 | 22/47 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.655×** | -5.0 | 7e-05 | 26/48 (C32, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.697×** | -4.4 | 9e-04 | 23/47 (HOP62, NCI-H2030, …) | all doses, flat | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.778×** | -4.3 | 0.001 | 24/48 (SNU-1, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.685×** | -4.3 | 0.001 | 17/33 (NCI-H2347, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.797×** | -3.9 | 0.005 | 23/48 (Panc 03.27, SNU-423, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.726×** | -3.9 | 0.005 | 19/45 (NCI-H460, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.735×** | -3.7 | 0.008 | 18/39 (KATO III, SNU-423, …) | all doses, flat | composition shift |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.746×** | -3.6 | 0.015 | 15/48 (A-172, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.738×** | -3.6 | 0.015 | 20/46 (SNU-423, C32, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.740×** | -3.5 | 0.016 | 18/30 (NCI-H1792, AsPC-1, …) | all doses, flat | composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.585×** | -3.4 | 0.023 | 14/44 (HCT15, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.757×** | -3.4 | 0.023 | 16/47 (NCI-H2030, A549, …) | all doses, flat | position effect removed |
| [[Megestrol (drug)]] 0.05 µM |  | **0.766×** | -3.2 | 0.037 | 13/48 (HOP62, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.768×** | -3.2 | 0.038 | 15/48 (MIA PaCa-2, SW48, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.754×** | -3.2 | 0.042 | 13/46 (COLO 205, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 906. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 30.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -20.3) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.218× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 18.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -12.4) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.185× (z -12.3) |
| [[C32 (line)]] | wt | 26.9 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0897× (z -15.2) |
| [[SNU-423 (line)]] | alt | 28.0 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.125× (z -12.4) ⚠ toxic |
| [[SW480 (line)]] | alt | 8.81 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.32× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 25.5 | 0 | 2 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0648× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 21.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +8.7) ⚠ cell-cycle shift, explains ~19% of this change | [[Dinaciclib (drug)]] 5 µM 0.147× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[BT-474 (line)]] | alt | 18.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 33.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.261× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 26.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.200× (z -10.6) |
| [[SNU-1 (line)]] | wt | 31.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.224× (z -8.9) ⚠ toxic |
| [[H4 (line)]] | wt | 23.4 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0825× (z -10.4) |
| [[KATO III (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -9.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 16.8 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.268× (z -10.6) |
| [[RKO (line)]] | wt | 26.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -8.8) |
| [[A-172 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 906), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NGLY1]] | +0.72 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[ENO2]] | +0.72 | +0.73 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_APOPTOSIS |
| [[FBXO42]] | +0.68 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[PIGH]] | +0.68 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[HILPDA]] | +0.66 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[DTNA]] | +0.66 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[DNAJC5]] | +0.66 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[GUK1]] | +0.64 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[ARID3A]] | +0.64 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[NDRG1]] | +0.64 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[PPFIA1]] | +0.64 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[GLTP]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP20]] | -0.64 | -0.63 / -0.55 | both halves | 1e-05 | same gene group |
| [[SNX5]] | -0.61 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ILF3]] | -0.61 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[TCF12]] | -0.61 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[TFAM]] | -0.60 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[TASOR]] | -0.59 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[TRIP12]] | -0.58 | -0.48 / -0.43 | both halves | 3e-05 | same gene group |
| [[FGD5-AS1]] | -0.58 | -0.56 / -0.40 | both halves | 4e-05 |  |
| [[BCLAF1]] | -0.57 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[MBNL3]] | -0.57 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[PARVA]] | -0.56 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[HNRNPF]] | -0.56 | -0.53 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PPP2R5B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MBNL3]] | B | MBNL3 activity lowers PPP2R5B's level | lines that do not express MBNL3 (16) vs lines expressing it (34) | 1.41× higher at baseline in the lines without MBNL3 | 0.046 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |
| [[SYT7]] | B | SYT7 activity lowers PPP2R5B's level | lines that do not express SYT7 (9) vs lines expressing it (41) | 1.16× higher at baseline in the lines without SYT7 | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RALGDS]] | C | PPP2R5B's natural level strengthens RALGDS's drug response | PPP2R5B's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.21; direction not clear | 0.078 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SMAP1]] | C | PPP2R5B's natural level strengthens SMAP1's drug response | PPP2R5B's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.16; direction not clear | 0.079 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 180]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.830). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.4, -14.9); signed map (-36.0, 25.9). **Vector** length 122, 32.3% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.4 | +5.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.1 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.0 | +7.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.7 | +5.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.4 | +5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.9 | +4.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.3 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +2.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.1 | +3.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.9 | -8.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.8 | -3.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.7 | -4.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.4 | -3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.3 | -1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.2 | -3.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 2 regulatory subunit B'beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,917,553-64,934,475 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35411, B56B, PR61B, B56beta |
| Gene groups (HGNC) | Protein phosphatase 2 regulatory subunits; Armadillo like helical domain containing |
| Hallmark sets | APOPTOSIS, HEME_METABOLISM |
| Reactome | 57 pathways, smallest: APC truncation mutants have impaired AXIN binding; AXIN missense mutants destabilize the destruction complex; Signaling by AMER1 mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15173](https://www.uniprot.org/uniprotkb/Q15173) (Serine/threonine-protein phosphatase 2A 56 kDa regulatory subunit beta isoform):

> As the regulatory component of the serine/threonine-protein phosphatase 2A (PP2A) holoenzyme, modulates substrate specificity, subcellular localization, and responsiveness to phosphorylation. The phosphorylated form mediates the interaction between PP2A and AKT1, leading to AKT1 dephosphorylation.

**Summary**, from NCBI Gene [5526](https://www.ncbi.nlm.nih.gov/gene/5526):

> The product of this gene belongs to the phosphatase 2A regulatory subunit B family. Protein phosphatase 2A is one of the four major Ser/Thr phosphatases, and it is implicated in the negative control of cell growth and division. It consists of a common heteromeric core enzyme, which is composed of a catalytic subunit and a constant regulatory subunit, that associates with a variety of regulatory subunits. The B regulatory subunit might modulate substrate selectivity and catalytic activity. This …

**Accessions** — [HGNC:9310](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9310) · Entrez [5526](https://www.ncbi.nlm.nih.gov/gene/5526) · UniProt [Q15173](https://www.uniprot.org/uniprotkb/Q15173) · Ensembl [ENSG00000068971](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068971)

## Data

Gene col 906: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 906); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 906, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 906]; `tensor/DDL_lfc|DDL_z.npy` [906]; `embed/gene_vectors.npy` [906]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 906 or target_col == 906). Every well: [[PPP2R5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP2R5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
