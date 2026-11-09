---
symbol: "BAP1"
type: "gene"
col: 8811
ensembl_id: "ENSG00000163930"
name: "BRCA1 associated deubiquitinase 1"
location: "3p21.1"
module: 127
arm: "+"
pooled_cpm: 16.87
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# BAP1

*BRCA1 associated deubiquitinase 1* — 3p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.15× (z +11.9, q 6e-30, up in 34 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 1.42× (z +3.9, q 0.008, up in 10 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 4.84×, HEC-1-A 2.80×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 4.07×, KATO III 3.91×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 3.90×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.666× (z -8.9, q 3e-16, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRPF31]] (+0.75, fdr 7e-06), [[ABCF3]] (+0.74, fdr 7e-06), [[MED16]] (+0.73, fdr 7e-06); moves opposite to [[ATP5F1E]] (-0.56, fdr 3e-05), [[HOTAIRM1]] (-0.54, fdr 1e-05), [[PHLDA2]] (-0.54, fdr 2e-05).
> It is in [[Module 127]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8811.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 4.84×, HEC-1-A 2.80×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 4.07×, KATO III 3.91×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 3.90×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +11.9 | 6e-30 | 34/41 (MIA PaCa-2, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +10.0 | 5e-21 | 28/37 (SK-MEL-2, KATO III, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +7.9 | 4e-13 | 7/48 (HOP62, AsPC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +7.9 | 4e-13 | 24/32 (LoVo, SW1417, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +7.1 | 2e-10 | 31/45 (SW1417, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.42×** | +3.9 | 0.008 | 10/47 (HCT15, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.16× | +3.3 | 0.074 | 11/48 (LOX-IMVI, RKO, …) | top dose only | low cells (technical?) |
| [[Docetaxel (drug)]] 5 µM |  | 1.16× | +3.2 | 0.094 | 4/48 (H4, RKO, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.2 | 0.094 | 6/33 (SW480, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.097 | 7/44 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 1.46× | +3.1 | 0.11 | 10/48 (RKO, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.31× | +3.0 | 0.12 | 12/45 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8811.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.666×** | -8.9 | 3e-16 | 35/47 (AsPC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.694×** | -5.7 | 4e-06 | 25/48 (C32, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.788×** | -5.2 | 3e-05 | 25/48 (SW1417, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.789×** | -5.2 | 3e-05 | 26/47 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.721×** | -5.1 | 5e-05 | 23/46 (SW48, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.705×** | -4.6 | 3e-04 | 20/47 (COLO 205, NCI-H1573, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.738×** | -4.5 | 5e-04 | 19/46 (SW48, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.756×** | -4.3 | 0.001 | 22/47 (MIA PaCa-2, HCT15, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.777×** | -3.9 | 0.006 | 18/48 (SW1417, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.780×** | -3.7 | 0.012 | 17/47 (A-427, HCT15, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.790×** | -3.7 | 0.013 | 16/47 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.803×** | -3.4 | 0.032 | 13/48 (C-33 A, hTERT-HPNE, …) | two highest doses | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.808×** | -3.3 | 0.042 | 13/47 (NCI-H460, Panc 03.27, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.786×** | -3.2 | 0.056 | 7/48 (KATO III, RPMI-7951, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.814×** | -3.2 | 0.056 | 16/47 (SW 900, KATO III, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Voriconazole (drug)]] 0.5 µM |  | **0.823×** | -3.0 | 0.093 | 5/48 (SW48, PANC-1, …) | two highest doses |  |
| [[Monocrotaline (drug)]] 0.5 µM |  | **0.826×** | -3.0 | 0.099 | 8/48 (NCI-H1573, H4, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.826×** | -3.0 | 0.099 | 9/47 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8811. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 16.4 | 0 | 2 | — | [[Acetohexamide (drug)]] 0.5 µM 0.0689× (z -11.8) |
| [[KATO III (line)]] | alt | 18.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.91× (z +9.2) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.245× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 18.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -10.3) |
| [[SW48 (line)]] | wt | 16.5 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 16.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -13.0) |
| [[CHP-212 (line)]] | wt | 19.0 | 0 | 1 | — | [[Pentagastrin (drug)]] 0.5 µM 0.0792× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 26.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +8.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 22.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -9.4) |
| [[LoVo (line)]] | wt | 13.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.90× (z +9.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 13.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.237× (z -10.0) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 12.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 25.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.07× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8811), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF31]] | +0.75 | +0.72 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[ABCF3]] | +0.74 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[MED16]] | +0.73 | +0.65 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[ATP13A1]] | +0.72 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[NOP9]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[ANAPC2]] | +0.71 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[SNRNP200]] | +0.70 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[DMAP1]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[PCNX3]] | +0.69 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[CDK16]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[USP19]] | +0.68 | +0.50 / +0.76 | both halves | 1e-05 | pathway: Deubiquitination |
| [[STK36]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5F1E]] | -0.56 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[HOTAIRM1]] | -0.54 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[PHLDA2]] | -0.54 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.876). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.7, -25.4); signed map (-12.2, -31.0). **Vector** length 81.0, 15.5% of its response variance represented; |z| ≥ 3 in 758 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.1 | +7.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +11.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.1 | +7.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +2.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[Folic acid (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +1.7 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -5.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.1 | -5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -2.7 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.0 | -2.8 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Adagrasib (drug)]] 5 µM |  | -2.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | BRCA1 associated deubiquitinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:52,401,008-52,410,008 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hucep-6, KIAA0272, UCHL2 |
| Gene groups (HGNC) | Ubiquitin C-terminal hydrolases |
| Reactome | 6 pathways, smallest: Recruitment and ATM-mediated phosphorylation of repair and signaling proteins at DNA double strand breaks; UCH proteinases; DNA Double Strand Break Response |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92560](https://www.uniprot.org/uniprotkb/Q92560) (Ubiquitin carboxyl-terminal hydrolase BAP1):

> Deubiquitinating enzyme that plays a key role in chromatin by mediating deubiquitination of histone H2A and HCFC1. Catalytic component of the polycomb repressive deubiquitinase (PR-DUB) complex, a complex that specifically mediates deubiquitination of histone H2A monoubiquitinated at 'Lys-120' (H2AK119ub1). Does not deubiquitinate monoubiquitinated histone H2B. The PR-DUB complex is an epigenetic regulator of gene expression and acts as a transcriptional coactivator, affecting genes involved in …

**Summary**, from NCBI Gene [8314](https://www.ncbi.nlm.nih.gov/gene/8314):

> This gene belongs to the ubiquitin C-terminal hydrolase subfamily of deubiquitinating enzymes that are involved in the removal of ubiquitin from proteins. The encoded enzyme binds to the breast cancer type 1 susceptibility protein (BRCA1) via the RING finger domain of the latter and acts as a tumor suppressor. In addition, the enzyme may be involved in regulation of transcription, regulation of cell cycle and growth, response to DNA damage and chromatin dynamics. Germline mutations in this gene …

**Accessions** — [HGNC:950](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:950) · Entrez [8314](https://www.ncbi.nlm.nih.gov/gene/8314) · UniProt [Q92560](https://www.uniprot.org/uniprotkb/Q92560) · Ensembl [ENSG00000163930](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163930)

## Data

Gene col 8811: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8811); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8811, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8811]; `tensor/DDL_lfc|DDL_z.npy` [8811]; `embed/gene_vectors.npy` [8811]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8811 or target_col == 8811). Every well: [[BAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
