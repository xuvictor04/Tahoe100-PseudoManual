---
symbol: "CLK2"
type: "gene"
col: 10720
ensembl_id: "ENSG00000176444"
name: "CDC like kinase 2"
location: "1q22"
module: 89
arm: "+"
pooled_cpm: 28.57
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# CLK2

*CDC like kinase 2* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.28× (z +8.6, q 4e-15, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.531× (z -12.2, q 2e-31, down in 24 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.698× (z -7.2, q 9e-11, down in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (HT-29 0.0834×, SW480 0.255×, A549 0.155×, HCT15 0.136×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1792 0.229×, NCI-H2347 0.290×, CHP-212 0.101×, KATO III 0.253×, …; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (SNU-1 0.112×, AsPC-1 0.189×; ⚠ toxic); [[Harringtonine (drug)]] 5 µM in 1 line (A498 0.321×); [[Acetazolamide (drug)]] 0.5 µM in 1 line (AN3 CA 0.0844×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.523×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF653]] (+0.60, fdr 2e-05), [[FZR1]] (+0.58, fdr 1e-05), [[ZNF333]] (+0.58, fdr 1e-05); moves opposite to [[ADSS2]] (-0.46, fdr 3e-05), [[TJP1]] (-0.45, fdr 4e-05), [[CDC42BPA]] (-0.45, fdr 1e-04).
> It is in [[Module 089]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10720.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.28×** | +8.6 | 4e-15 | 34/48 (NCI-H23, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.06×** | +7.6 | 1e-11 | 31/45 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +5.8 | 1e-06 | 21/48 (LoVo, A498, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +5.7 | 2e-06 | 25/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +5.6 | 3e-06 | 22/47 (NCI-H23, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +5.4 | 5e-06 | 23/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +5.1 | 3e-05 | 25/44 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +4.0 | 0.004 | 17/46 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Roxadustat (drug)]] 5 µM |  | 1.18× | +3.2 | 0.096 | 7/47 (NCI-H23, J82, …) | top dose only |  |
| [[Carbamazepine (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.12 | 9/47 (LoVo, NCI-H1792, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10720.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (HT-29 0.0834×, SW480 0.255×, A549 0.155×, HCT15 0.136×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1792 0.229×, NCI-H2347 0.290×, CHP-212 0.101×, KATO III 0.253×, …; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (SNU-1 0.112×, AsPC-1 0.189×; ⚠ toxic); [[Harringtonine (drug)]] 5 µM in 1 line (A498 0.321×); [[Acetazolamide (drug)]] 0.5 µM in 1 line (AN3 CA 0.0844×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.523×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.531×** | -12.2 | 2e-31 | 24/36 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.609×** | -9.9 | 8e-21 | 29/45 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.612×** | -9.5 | 6e-19 | 33/47 (SNU-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.698×** | -7.2 | 9e-11 | 28/47 (HCT15, BT-474, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.787×** | -4.6 | 4e-04 | 20/47 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.853× | -3.2 | 0.13 | 12/48 (NCI-H1573, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10720. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 27.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -11.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 32.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -10.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 50.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 38.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 56.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.461× (z -8.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 26.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -11.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 33.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -8.7) |
| [[A498 (line)]] | wt | 18.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.321× (z -9.4) |
| [[A549 (line)]] | wt | 26.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -13.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 23.3 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.5 µM 0.0844× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.189× (z -11.8) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 46.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -10.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -9.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 25.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -8.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.342× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change |
| [[HS-578T (line)]] | alt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 20.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0834× (z -16.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -10.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 34.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 60.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -9.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 24.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +10.3) | — |
| [[SNU-1 (line)]] | wt | 32.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.112× (z -12.8) ⚠ toxic |
| [[SW480 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -14.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10720), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF653]] | +0.60 | +0.69 / +0.49 | both halves | 2e-05 |  |
| [[FZR1]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ZNF333]] | +0.58 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[TRMU]] | +0.56 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[BCKDHA]] | +0.55 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[WRAP53]] | +0.55 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ZBTB48]] | +0.54 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[PMS2CL]] | +0.53 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[METTL22]] | +0.53 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[WDR89]] | +0.53 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[ZSCAN25]] | +0.52 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[TUT1]] | +0.52 | +0.44 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADSS2]] | -0.46 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[TJP1]] | -0.45 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[CDC42BPA]] | -0.45 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[PTPRK]] | -0.45 | -0.37 / -0.53 | both halves | 7e-05 |  |
| [[LIMS1]] | -0.44 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[SEPTIN11]] | -0.44 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[RABGAP1L]] | -0.44 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[YES1]] | -0.44 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[ARAP2]] | -0.43 | -0.44 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.395). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.1, -4.2); signed map (-35.4, 1.8). **Vector** length 79.2, 14.0% of its response variance represented; |z| ≥ 3 in 866 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.3 | +5.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.7 | +1.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +8.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +1.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.7 | -0.4 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.3 | -9.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -7.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.2 | -1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | CDC like kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,262,868-155,278,491 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | CDC like kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [P49760](https://www.uniprot.org/uniprotkb/P49760) (Dual specificity protein kinase CLK2):

> Dual specificity kinase acting on both serine/threonine and tyrosine-containing substrates. Phosphorylates serine- and arginine-rich (SR) proteins of the spliceosomal complex. May be a constituent of a network of regulatory mechanisms that enable SR proteins to control RNA splicing and can cause redistribution of SR proteins from speckles to a diffuse nucleoplasmic distribution. Acts as a suppressor of hepatic gluconeogenesis and glucose output by repressing PPARGC1A transcriptional activity on …

**Summary**, from NCBI Gene [1196](https://www.ncbi.nlm.nih.gov/gene/1196):

> This gene encodes a dual specificity protein kinase that phosphorylates serine/threonine and tyrosine-containing substrates. Activity of this protein regulates serine- and arginine-rich (SR) proteins of the spliceosomal complex, thereby influencing alternative transcript splicing. Chromosomal translocations have been characterized between this locus and the PAFAH1B3 (platelet-activating factor acetylhydrolase 1b, catalytic subunit 3 (29kDa)) gene on chromosome 19, resulting in the production of …

**Accessions** — [HGNC:2069](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2069) · Entrez [1196](https://www.ncbi.nlm.nih.gov/gene/1196) · UniProt [P49760](https://www.uniprot.org/uniprotkb/P49760) · Ensembl [ENSG00000176444](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176444)

## Data

Gene col 10720: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10720); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10720, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10720]; `tensor/DDL_lfc|DDL_z.npy` [10720]; `embed/gene_vectors.npy` [10720]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10720 or target_col == 10720). Every well: [[CLK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
