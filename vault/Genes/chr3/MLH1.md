---
symbol: "MLH1"
type: "gene"
col: 1146
ensembl_id: "ENSG00000076242"
name: "mutL homolog 1"
location: "3p22.2"
module: 148
arm: "+"
pooled_cpm: 24.09
n_lines_expressing: 47
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# MLH1

*mutL homolog 1* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.80× (z +14.3, q 1e-43, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.801× (z -5.5, q 3e-05, down in 25 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.0817×; ⚠ cell-cycle shift, explains ~49% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.106×; ⚠ transcription drop; cell-cycle shift, explains ~24% of this change); [[Vilanterol (drug)]] 0.5 µM in 1 line (COLO 205 0.0570×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (H4 0.310×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAGOHB]] (+0.72, fdr 7e-06), [[MIS12]] (+0.70, fdr 7e-06), [[COPS3]] (+0.68, fdr 1e-05); moves opposite to [[COMMD6]] (-0.63, fdr 2e-05), [[RPS14]] (-0.62, fdr 1e-05), [[TMEM276]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[NUP188]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1146.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +14.3 | 1e-43 | 38/45 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +9.9 | 9e-21 | 37/45 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +9.3 | 2e-18 | 36/45 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +6.4 | 2e-08 | 21/39 (LS 180, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.38×** | +5.5 | 3e-06 | 23/45 (A549, HCT15, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.37×** | +5.4 | 6e-06 | 24/44 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.34×** | +5.0 | 4e-05 | 20/41 (SNU-423, Panc 03.27, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.35×** | +5.0 | 4e-05 | 18/34 (NCI-H2347, A549, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.63×** | +4.4 | 6e-04 | 17/45 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +4.3 | 8e-04 | 19/45 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +3.9 | 0.005 | 17/45 (NCI-H1792, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.23×** | +3.4 | 0.031 | 17/44 (NCI-H460, A549, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.053 | 8/45 (LoVo, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.21×** | +3.2 | 0.057 | 13/45 (NCI-H460, A-427, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.13× | +3.1 | 0.081 | 19/44 (NCI-H460, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1146.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.0817×; ⚠ cell-cycle shift, explains ~49% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.106×; ⚠ transcription drop; cell-cycle shift, explains ~24% of this change); [[Vilanterol (drug)]] 0.5 µM in 1 line (COLO 205 0.0570×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (H4 0.310×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.801×** | -5.5 | 3e-05 | 25/45 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.768×** | -4.6 | 0.001 | 21/45 (HS-578T, SW 900, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | 0.829× | -3.2 | 0.21 | 15/44 (NCI-H661, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.833× | -3.2 | 0.21 | 10/45 (HS-578T, SK-MEL-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.832× | -3.1 | 0.25 | 8/44 (BT-474, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1146. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 23.6 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.310× (z -8.6) |
| [[J82 (line)]] | alt | 28.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.316× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 20.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.7) | — |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0570× (z -12.2) |
| [[hTERT-HPNE (line)]] | wt | 21.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.106× (z -13.1) ⚠ transcription drop; cell-cycle shift, explains ~24% of this change |
| [[LoVo (line)]] | wt | 22.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 33.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0817× (z -17.6) ⚠ cell-cycle shift, explains ~49% of this change |
| [[PANC-1 (line)]] | alt | 26.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.4) | — |
| [[A-172 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 28.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1146), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGOHB]] | +0.72 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[MIS12]] | +0.70 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[COPS3]] | +0.68 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[PSME3IP1]] | +0.66 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[VPS52]] | +0.65 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[MCM3AP]] | +0.64 | +0.47 / +0.64 | both halves | 2e-05 | pathway: Affinity selection of immunoglobulins |
| [[GEN1]] | +0.64 | +0.60 / +0.56 | both halves | 1e-05 | STRING 536 |
| [[PSMC3]] | +0.64 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[HNRNPL]] | +0.63 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[PEF1]] | +0.63 | +0.63 / +0.46 | both halves | 2e-05 |  |
| [[TSTD2]] | +0.63 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ALDH16A1]] | +0.63 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD6]] | -0.63 | -0.46 / -0.62 | both halves | 2e-05 |  |
| [[RPS14]] | -0.62 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[TMEM276]] | -0.62 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[RPS10]] | -0.61 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[CARHSP1]] | -0.61 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[RPL26]] | -0.61 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[RPL18]] ⚠ | -0.60 | -0.38 / -0.59 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MJ]] | -0.60 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[RPL23]] | -0.59 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[RPL34]] | -0.59 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[FNBP1L]] | -0.59 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[RPL17]] | -0.59 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[RPL27]] | -0.59 | -0.48 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUP188]] | C | MLH1 activity lowers NUP188's level | lines that do not express MLH1 (3) vs lines expressing it (47) | 2.77× higher at baseline in the lines without MLH1 | 0.011 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MLF1, ADAL, TTC30A |
| [[TSPAN33]] | C | MLH1 activity lowers TSPAN33's level | lines that do not express MLH1 (3) vs lines expressing it (47) | 4.40× higher at baseline in the lines without MLH1 | 0.028 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MLF1, ADAL, TTC30A |

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.747). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-36.3, -32.5); signed map (15.7, -27.6). **Vector** length 88.1, 18.6% of its response variance represented; |z| ≥ 3 in 851 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +6.7 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +6.5 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +14.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +1.4 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +1.6 | +2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +2.0 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +1.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.1 | -2.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.1 | -3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.1 | -4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | mutL homolog 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.2 — chr3:36,993,226-37,050,896 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HNPCC, FCC2, HNPCC2, MLH-1; previously COCA2 |
| Gene groups (HGNC) | MutL homologs; BRCA1-associated genome surveillance complex |
| Hallmark sets | E2F_TARGETS |
| Reactome | 17 pathways, smallest: Diseases of Mismatch Repair (MMR); Mismatch repair (MMR) directed by MSH2:MSH3 (MutSbeta); Mismatch repair (MMR) directed by MSH2:MSH6 (MutSalpha) |
| Matched by | ensembl_id |

**Function**, from UniProt [P40692](https://www.uniprot.org/uniprotkb/P40692) (DNA mismatch repair protein Mlh1):

> Heterodimerizes with PMS2 to form MutL alpha, a component of the post-replicative DNA mismatch repair system (MMR). DNA repair is initiated by MutS alpha (MSH2-MSH6) or MutS beta (MSH2-MSH3) binding to a dsDNA mismatch, then MutL alpha is recruited to the heteroduplex. Assembly of the MutL-MutS-heteroduplex ternary complex in presence of RFC and PCNA is sufficient to activate endonuclease activity of PMS2. It introduces single-strand breaks near the mismatch and thus generates new entry points …

**Summary**, from NCBI Gene [4292](https://www.ncbi.nlm.nih.gov/gene/4292):

> The protein encoded by this gene can heterodimerize with mismatch repair endonuclease PMS2 to form MutL alpha, part of the DNA mismatch repair system. When MutL alpha is bound by MutS beta and some accessory proteins, the PMS2 subunit of MutL alpha introduces a single-strand break near DNA mismatches, providing an entry point for exonuclease degradation. The encoded protein is also involved in DNA damage signaling and can heterodimerize with DNA mismatch repair protein MLH3 to form MutL gamma, …

**Accessions** — [HGNC:7127](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7127) · Entrez [4292](https://www.ncbi.nlm.nih.gov/gene/4292) · UniProt [P40692](https://www.uniprot.org/uniprotkb/P40692) · Ensembl [ENSG00000076242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076242)

## Data

Gene col 1146: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1146); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1146, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1146]; `tensor/DDL_lfc|DDL_z.npy` [1146]; `embed/gene_vectors.npy` [1146]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1146 or target_col == 1146). Every well: [[MLH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MLH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
