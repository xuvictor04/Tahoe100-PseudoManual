---
symbol: "MRPL48"
type: "gene"
col: 10625
ensembl_id: "ENSG00000175581"
name: "mitochondrial ribosomal protein L48"
location: "11q13.4"
module: 57
arm: "+"
pooled_cpm: 33.76
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# MRPL48

*mitochondrial ribosomal protein L48* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.51× (z +10.0, q 1e-20, up in 21 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.35× (z +7.6, q 4e-12, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.546× (z -21.5, q 0e+00, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FNTB]] (+0.61, fdr 2e-05), [[SDHB]] (+0.59, fdr 7e-06), [[PECR]] (+0.56, fdr 2e-05); moves opposite to [[ELF4]] (-0.47, fdr 3e-05), [[USP11]] (-0.47, fdr 2e-05), [[MED29]] (-0.46, fdr 1e-04).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10625.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +10.0 | 1e-20 | 21/38 (A549, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +8.8 | 2e-16 | 32/47 (SHP-77, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +8.6 | 2e-15 | 25/44 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +7.6 | 4e-12 | 28/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +7.6 | 4e-12 | 24/47 (HEC-1-A, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +6.8 | 1e-09 | 27/48 (SW480, NCI-H2347, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +6.2 | 5e-08 | 17/48 (KATO III, BT-474, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +6.1 | 7e-08 | 20/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +6.0 | 9e-08 | 21/47 (SHP-77, LS 180, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.27×** | +6.0 | 1e-07 | 19/48 (SNU-423, BT-474, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +5.7 | 5e-07 | 17/48 (SHP-77, SW48, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[EX229 (drug)]] 5 µM |  | **1.47×** | +5.1 | 2e-05 | 17/48 (AsPC-1, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change | **1.23×** | +4.8 | 6e-05 | 17/39 (HOP62, A549, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.43×** | +4.8 | 8e-05 | 16/48 (HT-29, HEC-1-A, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +4.3 | 6e-04 | 10/48 (A-427, AsPC-1, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.39×** | +4.3 | 6e-04 | 11/46 (SHP-77, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.001 | 10/48 (HEC-1-A, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.005 | 7/47 (LS 180, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.005 | 6/46 (NCI-H1792, NCI-H460, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.16× | +3.6 | 0.009 | 9/47 (A-427, AN3 CA, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10625.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.546×** | -21.5 | 0e+00 | 39/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.739×** | -10.7 | 2e-24 | 34/48 (LS 180, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.786×** | -6.1 | 2e-07 | 27/48 (SK-MEL-2, KATO III, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.794×** | -5.8 | 9e-07 | 23/47 (NCI-H661, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.818×** | -5.1 | 4e-05 | 17/48 (LS 180, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.826×** | -4.6 | 3e-04 | 20/48 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -4.1 | 0.003 | 11/48 (LS 180, NCI-H2347, …) | inconsistent across doses |  |
| [[Lapatinib ditosylate (drug)]] 0.05 µM |  | 0.861× | -3.6 | 0.025 | 9/48 (HCT15, SW480, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.765×** | -3.5 | 0.025 | 2/48 (SW480, Panc 03.27) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.878× | -3.3 | 0.058 | 18/47 (SW1417, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10625. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 68.7 | 4 (2 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 4.16× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.66× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -19.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 45.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -14.1) |
| [[A-427 (line)]] | wt | 36.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -10.4) |
| [[BT-474 (line)]] | alt | 68.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -10.5) |
| [[HCT15 (line)]] | alt | 41.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.102× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change |
| [[J82 (line)]] | alt | 35.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 25.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -9.7) |
| [[PANC-1 (line)]] | alt | 38.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -20.3) |
| [[SW48 (line)]] | wt | 61.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -8.8) |
| [[A549 (line)]] | wt | 17.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.29× (z +10.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 19.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -8.5) |
| [[C32 (line)]] | wt | 19.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 25.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -9.1) |
| [[H4 (line)]] | wt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -12.8) |
| [[Hs 766T (line)]] | wt | 34.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -11.4) |
| [[KATO III (line)]] | alt | 77.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -14.8) |
| [[LoVo (line)]] | wt | 33.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -17.8) |
| [[LS 180 (line)]] | wt | 62.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 30.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -12.8) |
| [[RPMI-7951 (line)]] | alt | 31.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -13.2) |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -13.3) |
| [[SNU-423 (line)]] | alt | 26.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -9.3) |
| [[SW480 (line)]] | alt | 49.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.607× (z -10.4) |
| [[A-172 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10625), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FNTB]] | +0.61 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[SDHB]] | +0.59 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[PECR]] | +0.56 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[CROT]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[LRIG2]] | +0.54 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[TNRC6A]] | +0.53 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[NDUFB6]] | +0.53 | +0.52 / +0.46 | both halves | 2e-05 | STRING 460 |
| [[NUP160]] | +0.53 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[COX16]] | +0.52 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[ZNF341]] | +0.52 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[GTF2H2B]] | +0.52 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[NDUFB7]] | +0.52 | +0.54 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELF4]] | -0.47 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[USP11]] | -0.47 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[MED29]] | -0.46 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[DPH1-AS1]] | -0.46 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[NFATC1]] | -0.46 | -0.52 / -0.37 | both halves | 7e-05 |  |
| [[CHD4]] | -0.46 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[CDC37]] | -0.45 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[HIVEP2-DT]] | -0.45 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[YES1]] | -0.45 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[ZNF597]] | -0.45 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[ERI2]] | -0.44 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[PPP1R18]] | -0.44 | -0.35 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.433). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-2.9, -11.3); signed map (-33.2, -11.7). **Vector** length 96.7, 20.4% of its response variance represented; |z| ≥ 3 in 826 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +6.7 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +8.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.3 | +6.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +4.2 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +7.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.8 | -21.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.1 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -6.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.7 | -5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -10.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -2.8 |
|  | [[Infigratinib (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.6 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L48 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:73,787,872-73,865,133 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-118, mL48 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q96GC5](https://www.uniprot.org/uniprotkb/Q96GC5) carries no function annotation.

**Summary**, from NCBI Gene [51642](https://www.ncbi.nlm.nih.gov/gene/51642):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:16653](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16653) · Entrez [51642](https://www.ncbi.nlm.nih.gov/gene/51642) · UniProt [Q96GC5](https://www.uniprot.org/uniprotkb/Q96GC5) · Ensembl [ENSG00000175581](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175581)

## Data

Gene col 10625: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10625); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10625, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10625]; `tensor/DDL_lfc|DDL_z.npy` [10625]; `embed/gene_vectors.npy` [10625]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10625 or target_col == 10625). Every well: [[MRPL48 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL48.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
