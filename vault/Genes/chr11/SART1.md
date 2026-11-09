---
symbol: "SART1"
type: "gene"
col: 10612
ensembl_id: "ENSG00000175467"
name: "spliceosome associated factor 1, recruiter of U4/U6.U5 tri-snRNP"
location: "11q13.1"
module: 52
arm: "+"
pooled_cpm: 54.02
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# SART1

*spliceosome associated factor 1, recruiter of U4/U6.U5 tri-snRNP* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.33× (z +18.9, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Carbidopa (monohydrate) (drug)]] 0.05 µM: 0.702× (z -5.1, q 2e-04, down in 37 of 48 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.813× (z -4.6, q 0.001, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.280×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF40]] (+0.64, fdr 1e-05), [[PRPF6]] (+0.63, fdr 1e-05), [[EDC3]] (+0.62, fdr 2e-05); moves opposite to [[PEAK1]] (-0.52, fdr 5e-05), [[ATP1B3]] (-0.51, fdr 4e-05), [[ARL15]] (-0.50, fdr 7e-05).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10612.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.33×** | +18.9 | 0e+00 | 44/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.78×** | +12.9 | 1e-35 | 48/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.00×** | +10.9 | 2e-25 | 41/48 (RPMI-7951, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.70×** | +10.8 | 5e-25 | 45/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +6.1 | 1e-07 | 33/48 (LOX-IMVI, SNU-423, …) | two highest doses | cell-cycle shift (explains ~20% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.46×** | +5.9 | 3e-07 | 33/48 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.42×** | +5.5 | 2e-06 | 27/48 (RKO, SW480, …) | two highest doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +5.5 | 3e-06 | 35/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.44×** | +5.3 | 6e-06 | 25/44 (SW480, SNU-423, …) | inconsistent across doses | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.2 | 1e-05 | 31/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.36×** | +4.7 | 2e-04 | 29/48 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.32×** | +4.4 | 5e-04 | 29/47 (PANC-1, NCI-H1573, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +4.4 | 6e-04 | 26/48 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.28×** | +3.9 | 0.005 | 24/48 (SNU-423, RKO, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.011 | 21/48 (SNU-423, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.011 | 20/48 (A-172, SW480, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.019 | 21/48 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.048 | 17/47 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +2.9 | 0.093 | 18/48 (A-427, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10612.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.280×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.702×** | -5.1 | 2e-04 | 37/48 (SW480, A-427, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.813×** | -4.6 | 0.001 | 22/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.779×** | -4.0 | 0.012 | 25/48 (HOP62, HT-29, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.839× | -3.9 | 0.012 | 24/48 (HS-578T, A-427, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10612. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 70.4 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +11.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.51× (z +11.7) | — |
| [[NCI-H1573 (line)]] | alt | 54.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +18.7) | — |
| [[HEC-1-A (line)]] | alt | 42.0 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.56× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 47.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +22.7) | — |
| [[LS 180 (line)]] | wt | 39.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +10.2) | — |
| [[SW480 (line)]] | alt | 62.5 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.66× (z +11.7) | — |
| [[A-427 (line)]] | wt | 61.2 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.22× (z +9.1) | — |
| [[C32 (line)]] | wt | 43.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +12.9) | — |
| [[HOP62 (line)]] | alt | 35.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +27.2) | — |
| [[Hs 766T (line)]] | wt | 52.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +14.9) | — |
| [[HS-578T (line)]] | alt | 73.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +19.9) | — |
| [[KATO III (line)]] | alt | 55.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 45.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +15.0) | — |
| [[NCI-H460 (line)]] | wt | 30.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +17.1) | — |
| [[Panc 03.27 (line)]] | alt | 76.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.5) | — |
| [[RKO (line)]] | wt | 42.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.04× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 67.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.64× (z +21.3) | — |
| [[SW48 (line)]] | wt | 39.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.76× (z +15.0) | — |
| [[A-172 (line)]] | wt | 35.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.5) | — |
| [[A549 (line)]] | wt | 55.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.8) | — |
| [[BT-474 (line)]] | alt | 57.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 47.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +12.6) | — |
| [[COLO 205 (line)]] | alt | 40.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +9.8) | — |
| [[H4 (line)]] | wt | 56.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +12.7) | — |
| [[HepG2_C3A (line)]] | wt | 32.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 49.6 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 46.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +13.8) | — |
| [[NCI-H1792 (line)]] | alt | 37.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +16.1) | — |
| [[NCI-H23 (line)]] | alt | 57.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +12.5) | — |
| [[SNU-423 (line)]] | alt | 44.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +20.0) | — |
| [[SW 900 (line)]] | alt | 57.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.8) | — |
| [[A498 (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 83.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10612), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF40]] | +0.64 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[PRPF6]] | +0.63 | +0.71 / +0.51 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 999 |
| [[EDC3]] | +0.62 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[C19orf47]] | +0.62 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[SUPT5H]] | +0.62 | +0.72 / +0.46 | both halves | 3e-05 | STRING 467 |
| [[UVSSA]] | +0.62 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[NEURL4]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[SF3A3]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 999 |
| [[CCDC9]] | +0.60 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[ZNF417]] | +0.59 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[AAAS]] | +0.58 | +0.70 / +0.33 | both halves | 1e-04 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[FOXRED1]] | +0.58 | +0.61 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEAK1]] | -0.52 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[ATP1B3]] | -0.51 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[ARL15]] | -0.50 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[MEMO1]] | -0.46 | -0.52 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.500). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-34.6, -4.3); signed map (-12.6, -24.7). **Vector** length 88.5, 22.2% of its response variance represented; |z| ≥ 3 in 945 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +5.2 | +5.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.0 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | +4.5 | +2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +18.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +10.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +4.4 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +2.6 | +1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +3.2 |
|  | [[Oxaliplatin (drug)]] 0.05 µM |  | +2.0 | +1.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -4.6 | -3.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.4 | -0.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -4.3 | +4.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | +2.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -4.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | +0.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -1.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | spliceosome associated factor 1, recruiter of U4/U6.U5 tri-snRNP |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,961,728-65,980,137 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Ara1, Snu66, SNRNP110, HAF |
| Gene groups (HGNC) | tri-snRP complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O43290](https://www.uniprot.org/uniprotkb/O43290) (U4/U6.U5 tri-snRNP-associated protein 1):

> Plays a role in mRNA splicing as a component of the U4/U6-U5 tri-snRNP, one of the building blocks of the spliceosome. May also bind to DNA.

**Summary**, from NCBI Gene [9092](https://www.ncbi.nlm.nih.gov/gene/9092):

> This gene encodes two proteins, the SART1(800) protein expressed in the nucleus of the majority of proliferating cells, and the SART1(259) protein expressed in the cytosol of epithelial cancers. The SART1(259) protein is translated by the mechanism of -1 frameshifting during posttranscriptional regulation; its full-length sequence is not published yet. The two encoded proteins are thought to be involved in the regulation of proliferation. Both proteins have tumor-rejection antigens. The …

**Accessions** — [HGNC:10538](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10538) · Entrez [9092](https://www.ncbi.nlm.nih.gov/gene/9092) · UniProt [O43290](https://www.uniprot.org/uniprotkb/O43290) · Ensembl [ENSG00000175467](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175467)

## Data

Gene col 10612: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10612); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10612, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10612]; `tensor/DDL_lfc|DDL_z.npy` [10612]; `embed/gene_vectors.npy` [10612]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10612 or target_col == 10612). Every well: [[SART1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SART1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
