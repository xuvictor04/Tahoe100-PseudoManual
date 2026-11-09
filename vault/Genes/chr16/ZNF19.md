---
symbol: "ZNF19"
type: "gene"
col: 8070
ensembl_id: "ENSG00000157429"
name: "zinc finger protein 19"
location: "16q22.2"
module: 10
arm: "+"
pooled_cpm: 6.18
n_lines_expressing: 49
n_dd_up: 32
n_dd_down: 13
n_dd_up_clean: 25
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ZNF19

*zinc finger protein 19* — 16q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.79× (z +11.0, q 3e-25, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.386× (z -9.8, q 8e-20, down in 25 of 34 measured lines) ⚠ toxic. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.503× (z -7.3, q 3e-11, down in 26 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00412]] (+0.67, fdr 7e-06), [[ETFRF1]] (+0.62, fdr 8e-06), [[TIGD6]] (+0.60, fdr 1e-05); moves opposite to [[BRI3BP]] (-0.52, fdr 5e-05), [[SLC2A13]] (-0.51, fdr 3e-05), [[VDAC1]] (-0.50, fdr 2e-05).
> It sits in the **+** arm of [[Module 010]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8070.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.79×** | +11.0 | 3e-25 | 38/46 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.47×** | +9.7 | 1e-19 | 36/44 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +8.5 | 5e-15 | 6/12 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +8.4 | 9e-15 | 27/40 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.65×** | +7.5 | 5e-12 | 19/46 (NCI-H2030, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.97×** | +7.3 | 3e-11 | 28/46 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.81×** | +6.4 | 2e-08 | 21/45 (RKO, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +6.3 | 3e-08 | 9/26 (HOP62, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.75×** | +6.0 | 2e-07 | 23/46 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.46×** | +5.7 | 6e-07 | 17/45 (RKO, LS 180, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +5.5 | 2e-06 | 20/40 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +5.4 | 4e-06 | 7/18 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **1.38×** | +4.7 | 1e-04 | 12/45 (SW480, NCI-H2030, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.54×** | +4.5 | 3e-04 | 14/43 (SW480, A549, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **2.18×** | +4.4 | 5e-04 | 9/43 (SW480, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +4.3 | 6e-04 | 15/39 (RKO, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.014 | 7/44 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.27×** | +3.5 | 0.014 | 11/46 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.84×** | +3.4 | 0.019 | 3/44 (SW480, HEC-1-A, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8070.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.386×** | -9.8 | 8e-20 | 25/34 (NCI-H2030, RKO, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.431×** | -9.0 | 7e-17 | 30/46 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.471×** | -8.0 | 2e-13 | 25/38 (HT-29, SW1417, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.503×** | -7.3 | 3e-11 | 26/44 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.662×** | -4.4 | 0.001 | 18/45 (SW480, SW 900, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.671×** | -4.3 | 0.002 | 12/42 (LOX-IMVI, A-172, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.469×** | -4.2 | 0.002 | 10/41 (COLO 205, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.765×** | -4.0 | 0.004 | 14/46 (J82, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | **0.715×** | -3.6 | 0.021 | 9/41 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.724×** | -3.5 | 0.031 | 18/44 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.714×** | -3.4 | 0.036 | 14/44 (CHP-212, SNU-1, …) | inconsistent across doses |  |
| [[Fluvoxamine (maleate) (drug)]] 5 µM |  | **0.809×** | -3.2 | 0.066 | 6/45 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.745×** | -3.1 | 0.074 | 14/46 (SW480, C-33 A, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.672× | -3.0 | 0.10 | 4/47 (A498, SW480, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8070. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 13.6 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0766× (z -15.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.196× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 6.35 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +9.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0860× (z -10.1) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.137× (z -8.5) |
| [[PANC-1 (line)]] | alt | 5.04 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.139× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 15.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0579× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Monocrotaline (drug)]] 0.05 µM 0.105× (z -8.5) |
| [[HT-29 (line)]] | alt | 9.33 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0533× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 9.13 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.141× (z -8.5) ⚠ toxic |
| [[BT-474 (line)]] | alt | 6.33 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 0.05 µM 0.0676× (z -8.6) |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[COLO 205 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HCT15 (line)]] | alt | 7.85 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0499× (z -8.9) |
| [[HOP62 (line)]] | alt | 4.65 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.0× (z +9.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 4.56 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0613× (z -9.7) |
| [[RKO (line)]] | wt | 8.83 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.112× (z -9.2) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0827× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 7.72 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0676× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8070), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00412]] | +0.67 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ETFRF1]] | +0.62 | +0.65 / +0.57 | both halves | 8e-06 |  |
| [[TIGD6]] | +0.60 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[CD72]] | +0.58 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[COQ5]] | +0.58 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[ZSCAN21]] | +0.58 | +0.67 / +0.45 | both halves | 3e-05 | same gene group |
| [[LINC02340]] | +0.57 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[AHI1-DT]] | +0.57 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[ZNF407-AS1]] | +0.56 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[TMEM30A-DT]] | +0.56 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[TMEM128]] | +0.56 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ZNF594]] | +0.56 | +0.67 / +0.48 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRI3BP]] | -0.52 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[SLC2A13]] | -0.51 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[VDAC1]] | -0.50 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[AMD1]] | -0.50 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[ARHGEF26]] | -0.50 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[LMBR1]] | -0.49 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[NT5DC3]] | -0.48 | -0.43 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.563). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (1.9, 12.9); signed map (10.8, -20.9). **Vector** length 54.0, 7.61% of its response variance represented; |z| ≥ 3 in 958 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.2 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +7.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +6.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -4.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.7 | -4.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -1.7 | -9.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -2.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -3.0 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.2 — chr16:71,464,555-71,565,089 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KOX12, MGC51021 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P17023](https://www.uniprot.org/uniprotkb/P17023) (Zinc finger protein 19):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7567](https://www.ncbi.nlm.nih.gov/gene/7567):

> The protein encoded by this gene contains a zinc finger, a nucleic acid-binding domain present in many transcription factors. This gene is located in a region next to ZNF23, a gene also encoding a zinc finger protein, on chromosome 16. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12981](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12981) · Entrez [7567](https://www.ncbi.nlm.nih.gov/gene/7567) · UniProt [P17023](https://www.uniprot.org/uniprotkb/P17023) · Ensembl [ENSG00000157429](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157429)

## Data

Gene col 8070: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8070); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8070, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8070]; `tensor/DDL_lfc|DDL_z.npy` [8070]; `embed/gene_vectors.npy` [8070]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8070 or target_col == 8070). Every well: [[ZNF19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
