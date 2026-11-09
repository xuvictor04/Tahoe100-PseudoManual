---
symbol: "SPA17"
type: "gene"
col: 739
ensembl_id: "ENSG00000064199"
name: "sperm autoantigenic protein 17"
location: "11q24.2"
module: 22
arm: "+"
pooled_cpm: 7.27
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# SPA17

*sperm autoantigenic protein 17* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.41× (z +13.7, q 4e-40, up in 9 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.27× (z +7.9, q 4e-13, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.651× (z -4.1, q 0.021, down in 15 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-901 (drug)]] 0.05 µM: 0.669× (z -3.7, q 0.072, down in 16 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0620×; ⚠ cell-cycle shift, explains ~0% of this change); [[Triamcinolone (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0608×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDKN3]] (+0.60, fdr 1e-05), [[CENPE]] (+0.59, fdr 1e-05), [[DEPDC1]] (+0.58, fdr 1e-05); moves opposite to [[IL17RA]] (-0.49, fdr 2e-04), [[RABEPK]] (-0.46, fdr 7e-05), [[ZFAS1]] (-0.45, fdr 1e-04).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 739.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.41×** | +13.7 | 4e-40 | 9/9 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.96×** | +13.2 | 2e-37 | 29/30 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.78×** | +8.3 | 3e-14 | 16/18 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.27×** | +7.9 | 4e-13 | 34/46 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.94×** | +6.4 | 2e-08 | 31/46 (KATO III, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.83×** | +5.8 | 6e-07 | 23/46 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **1.68×** | +5.0 | 5e-05 | 18/33 (HOP62, NCI-H1792, …) | all doses, flat | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.43×** | +4.9 | 8e-05 | 24/47 (NCI-H1792, HEC-1-A, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.61×** | +4.6 | 3e-04 | 18/38 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +4.3 | 0.001 | 16/46 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.52×** | +3.9 | 0.005 | 13/44 (KATO III, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +3.9 | 0.005 | 16/42 (KATO III, NCI-H2030, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.009 | 20/46 (RKO, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.025 | 12/46 (NCI-H1573, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.028 | 12/41 (LOX-IMVI, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Filgotinib (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.090 | 2/46 (PANC-1, SW480) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.36×** | +3.0 | 0.099 | 7/46 (SW480, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 739.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0620×; ⚠ cell-cycle shift, explains ~0% of this change); [[Triamcinolone (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0608×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.651×** | -4.1 | 0.021 | 15/46 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.669×** | -3.7 | 0.072 | 16/46 (AN3 CA, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.705× | -3.4 | 0.14 | 16/46 (PANC-1, NCI-H661, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.785× | -3.3 | 0.14 | 12/47 (LS 180, HepG2/C3A, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.723× | -3.1 | 0.20 | 16/46 (NCI-H2030, HepG2/C3A, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.547× | -3.0 | 0.21 | 12/39 (PANC-1, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~73% of this change | 0.718× | -3.0 | 0.21 | 13/43 (PANC-1, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 739. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 12.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.53× (z +9.3) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 16.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 6.95 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.39× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 6.09 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.05 µM 0.0608× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 5.86 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0620× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 6.85 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 8.99× (z +8.8) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 6.45 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.0× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 739), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN3]] | +0.60 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[CENPE]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[DEPDC1]] | +0.58 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SCLT1]] | +0.58 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[G2E3]] | +0.58 | +0.38 / +0.60 | both halves | 6e-05 |  |
| [[CENPF]] | +0.58 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[CCNB1]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[CKAP2]] | +0.56 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[ASPM]] | +0.56 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[DLGAP5]] | +0.56 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[NEK2]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[ACBD7]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL17RA]] | -0.49 | -0.61 / -0.31 | both halves | 2e-04 |  |
| [[RABEPK]] | -0.46 | -0.51 / -0.37 | both halves | 7e-05 |  |
| [[ZFAS1]] | -0.45 | -0.34 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.535). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.7, -57.2); signed map (-51.2, -44.1). **Vector** length 54.3, 8.39% of its response variance represented; |z| ≥ 3 in 770 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Activation of NIMA Kinases NEK9, NEK6, NEK7* (reactome, mean cos +0.51 to 4); *Golgi Cisternae Pericentriolar Stack Reorganization* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +4.2 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +13.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.3 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +3.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.1 | +2.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.0 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~73% of this change | -2.3 | -3.0 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -1.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -2.2 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | sperm autoantigenic protein 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:124,673,844-124,697,518 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SP17, CT22 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15506](https://www.uniprot.org/uniprotkb/Q15506) (Sperm surface protein Sp17):

> Sperm surface zona pellucida binding protein. Helps to bind spermatozoa to the zona pellucida with high affinity. Might function in binding zona pellucida and carbohydrates (By similarity).

**Summary**, from NCBI Gene [53340](https://www.ncbi.nlm.nih.gov/gene/53340):

> This gene encodes a protein present at the cell surface. The N-terminus has sequence similarity to human cAMP-dependent protein kinase A (PKA) type II alpha regulatory subunit (RIIa) while the C-terminus has an IQ calmodulin-binding motif. The central portion of the protein has carbohydrate binding motifs and likely functions in cell-cell adhesion. The protein was initially characterized by its involvement in the binding of sperm to the zona pellucida of the oocyte. Recent studies indicate that …

**Accessions** — [HGNC:11210](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11210) · Entrez [53340](https://www.ncbi.nlm.nih.gov/gene/53340) · UniProt [Q15506](https://www.uniprot.org/uniprotkb/Q15506) · Ensembl [ENSG00000064199](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064199)

## Data

Gene col 739: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 739); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 739, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 739]; `tensor/DDL_lfc|DDL_z.npy` [739]; `embed/gene_vectors.npy` [739]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 739 or target_col == 739). Every well: [[SPA17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPA17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
