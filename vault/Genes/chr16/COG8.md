---
symbol: "COG8"
type: "gene"
col: 13100
ensembl_id: "ENSG00000213380"
name: "component of oligomeric golgi complex 8"
location: "16q22.1"
module: 4
arm: "+"
pooled_cpm: 21.73
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# COG8

*component of oligomeric golgi complex 8* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.73× (z +9.7, q 2e-19, up in 22 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.28× (z +4.6, q 7e-04, up in 16 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.645× (z -11.4, q 3e-27, down in 35 of 47 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.593× (z -9.6, q 2e-19, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSU72]] (+0.69, fdr 7e-06), [[ZFP62]] (+0.68, fdr 7e-06), [[PFAS]] (+0.65, fdr 7e-06); moves opposite to [[STX12]] (-0.61, fdr 1e-05), [[SELENOK]] (-0.59, fdr 2e-05), [[SELENOW]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13100.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +9.7 | 2e-19 | 22/32 (SW1417, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +7.1 | 3e-10 | 21/39 (LS 180, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +6.5 | 1e-08 | 25/42 (RPMI-7951, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.6 | 7e-04 | 16/48 (KATO III, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.24×** | +3.9 | 0.009 | 18/45 (HOP62, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.009 | 13/48 (A498, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.013 | 12/48 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +3.7 | 0.017 | 10/47 (PANC-1, LoVo, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.6 | 0.024 | 9/48 (A498, hTERT-HPNE, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.031 | 12/48 (A-172, NCI-H1792, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.082 | 12/47 (A549, A498, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.098 | 11/48 (SHP-77, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13100.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.645×** | -11.4 | 3e-27 | 35/47 (A-427, NCI-H460, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.593×** | -9.6 | 2e-19 | 33/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.600×** | -9.4 | 9e-19 | 35/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.630×** | -8.5 | 3e-15 | 31/47 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.645×** | -7.8 | 9e-13 | 28/48 (NCI-H460, SNU-1, …) | top dose only | cell-cycle shift (explains ~21% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.673×** | -7.3 | 3e-11 | 24/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.725×** | -5.6 | 2e-06 | 25/48 (A498, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.751×** | -5.3 | 1e-05 | 22/47 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.755×** | -5.2 | 1e-05 | 20/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.607×** | -4.8 | 9e-05 | 16/39 (A498, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.771×** | -4.8 | 9e-05 | 16/48 (SW480, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.830×** | -3.4 | 0.031 | 8/48 (NCI-H2030, HepG2/C3A, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.711×** | -3.3 | 0.045 | 11/46 (J82, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.844× | -3.1 | 0.072 | 12/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.789×** | -3.1 | 0.073 | 5/48 (SW480, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 0.05 µM |  | 0.836× | -3.0 | 0.084 | 12/47 (HCT15, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13100. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -10.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.332× (z -9.3) |
| [[SW480 (line)]] | alt | 53.6 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.251× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.415× (z -8.9) |
| [[A-427 (line)]] | wt | 24.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -14.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[AsPC-1 (line)]] | alt | 8.65 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0972× (z -9.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.193× (z -10.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 37.9 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0818× (z -10.2) |
| [[HT-29 (line)]] | alt | 23.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.283× (z -9.4) |
| [[LoVo (line)]] | wt | 25.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.338× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.288× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[NCI-H23 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.287× (z -8.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -9.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[PANC-1 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -10.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[RKO (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.189× (z -9.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 23.1 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.226× (z -9.1) |
| [[A-172 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13100), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSU72]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[ZFP62]] | +0.68 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[PFAS]] | +0.65 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[PRPF19]] | +0.64 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[C1QBP]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[ATIC]] | +0.61 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[MRPL3]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SF3B3]] | +0.60 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[MYBBP1A]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[HNRNPF]] | +0.59 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[TBL3]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[URB2]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX12]] | -0.61 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[SELENOK]] | -0.59 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[SELENOW]] | -0.57 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[WDR44]] | -0.56 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[COX17]] | -0.55 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[BLVRB]] | -0.55 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[IFI27L2]] | -0.54 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[GABARAPL2]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[UQCRB]] ⚠ | -0.53 | -0.46 / -0.50 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CCS]] | -0.53 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ROMO1]] | -0.53 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[TRNAU1AP]] | -0.52 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[ATP5PD]] | -0.52 | -0.33 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.611). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-21.0, -35.2); signed map (-5.4, -42.8). **Vector** length 62.7, 9.78% of its response variance represented; |z| ≥ 3 in 850 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +3.3 | -2.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.5 | +1.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.3 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +4.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.6 | -11.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -4.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.6 | -3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | component of oligomeric golgi complex 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:69,320,140-69,339,583 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22315, DOR1 |
| Gene groups (HGNC) | Components of oligomeric golgi complex |
| Reactome | 9 pathways, smallest: Intra-Golgi traffic; Retrograde transport at the Trans-Golgi-Network; COPI-mediated anterograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MW5](https://www.uniprot.org/uniprotkb/Q96MW5) (Conserved oligomeric Golgi complex subunit 8):

> Required for normal Golgi function.

**Summary**, from NCBI Gene [84342](https://www.ncbi.nlm.nih.gov/gene/84342):

> This gene encodes a protein that is a component of the conserved oligomeric Golgi (COG) complex, a multiprotein complex that plays a structural role in the Golgi apparatus, and is involved in intracellular membrane trafficking and glycoprotein modification. Mutations in this gene cause congenital disorder of glycosylation, type IIh, a disease that is characterized by under-glycosylated serum proteins, and whose symptoms include severe psychomotor retardation, failure to thrive, seizures, and …

**Accessions** — [HGNC:18623](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18623) · Entrez [84342](https://www.ncbi.nlm.nih.gov/gene/84342) · UniProt [Q96MW5](https://www.uniprot.org/uniprotkb/Q96MW5) · Ensembl [ENSG00000213380](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213380)

## Data

Gene col 13100: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13100); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13100, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13100]; `tensor/DDL_lfc|DDL_z.npy` [13100]; `embed/gene_vectors.npy` [13100]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13100 or target_col == 13100). Every well: [[COG8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COG8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
