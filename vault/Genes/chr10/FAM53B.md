---
symbol: "FAM53B"
type: "gene"
col: 12115
ensembl_id: "ENSG00000189319"
name: "family with sequence similarity 53 member B"
location: "10q26.13"
module: 1
arm: "+"
pooled_cpm: 25.12
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 4
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# FAM53B

*family with sequence similarity 53 member B* — 10q26.13

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.44× (z +4.3, q 0.011, up in 23 of 48 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 3.29×; ⚠ cell-cycle shift, explains ~18% of this change).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.633× (z -5.0, q 3e-04, down in 21 of 41 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (hTERT-HPNE 0.128×, NCI-H460 0.260×, SK-MEL-2 0.177×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.141×, SK-MEL-2 0.172×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (KATO III 0.0959×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Oxaprozin (drug)]] 0.5 µM in 1 line (BT-474 0.0924×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (BT-474 0.103×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (CHP-212 0.0861×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX5]] (+0.58, fdr 1e-05), [[HCFC1]] (+0.57, fdr 4e-05), [[ANAPC1]] (+0.57, fdr 1e-05); moves opposite to [[POLD4]] (-0.61, fdr 1e-05), [[CTTNBP2NL]] (-0.61, fdr 1e-05), [[VEZT]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RASSF8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12115.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 3.29×; ⚠ cell-cycle shift, explains ~18% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.44×** | +4.3 | 0.011 | 23/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12115.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (hTERT-HPNE 0.128×, NCI-H460 0.260×, SK-MEL-2 0.177×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.141×, SK-MEL-2 0.172×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (KATO III 0.0959×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Oxaprozin (drug)]] 0.5 µM in 1 line (BT-474 0.0924×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (BT-474 0.103×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (CHP-212 0.0861×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.633×** | -5.0 | 3e-04 | 21/41 (hTERT-HPNE, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.661×** | -4.9 | 3e-04 | 25/44 (NCI-H1573, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.705×** | -4.0 | 0.013 | 25/48 (H4, J82, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.725×** | -3.8 | 0.021 | 21/48 (AN3 CA, SW48, …) | all doses, stronger at high dose | position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.761× | -3.2 | 0.14 | 15/46 (CFPAC-1, A549, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.833× | -3.1 | 0.21 | 22/48 (A-427, A-172, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12115. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 33.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -13.6) ⚠ cell-cycle shift, explains ~72% of this change |
| [[AN3 CA (line)]] | alt | 62.0 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0607× (z -11.7) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0947× (z -9.1) |
| [[BT-474 (line)]] | alt | 12.8 | 0 | 2 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0924× (z -11.2) |
| [[KATO III (line)]] | alt | 43.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0959× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SK-MEL-2 (line)]] | alt | 32.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 17.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +10.1) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[CHP-212 (line)]] | wt | 45.4 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0861× (z -9.7) |
| [[HCT15 (line)]] | alt | 38.0 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.194× (z -9.3) ⚠ cell-cycle shift, explains ~5% of this change |
| [[hTERT-HPNE (line)]] | wt | 28.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H460 (line)]] | wt | 28.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -9.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 33.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12115), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX5]] | +0.58 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[HCFC1]] | +0.57 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[ANAPC1]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[TRRAP]] | +0.56 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[DUS3L]] | +0.54 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[PRDM15]] | +0.54 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[NDUFA10]] | +0.52 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[U2AF2]] | +0.52 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[COX10]] | +0.52 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[RAI1]] | +0.51 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[MFN2]] | +0.51 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[KMT2D]] | +0.51 | +0.32 / +0.42 | both halves | 1e-04 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLD4]] | -0.61 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[CTTNBP2NL]] | -0.61 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[VEZT]] | -0.56 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[FGD6]] | -0.53 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[DNTTIP1]] | -0.52 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[UGCG]] | -0.52 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[UBE2B]] | -0.51 | -0.44 / -0.43 | both halves | 4e-05 |  |
| [[SNAP29]] | -0.50 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[KLF7]] | -0.50 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[ZNF212]] | -0.50 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[KIFAP3]] | -0.50 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[CDKN2D]] | -0.49 | -0.39 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASSF8]] | B | RASSF8 activity raises FAM53B's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 1.09× lower at baseline in the lines without RASSF8 | 0.037 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.235). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-2.5, 5.4); signed map (-9.7, -39.3). **Vector** length 83.8, 17.0% of its response variance represented; |z| ≥ 3 in 837 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.7 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +3.4 | -2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +3.3 | +2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.2 | +1.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +1.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +1.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -3.0 | -4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -0.7 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | +0.0 |
|  | [[Bexarotene (drug)]] 5 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 53 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.13 — chr10:124,619,292-124,744,378 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA12J10.2, smp; previously KIAA0140 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14153](https://www.uniprot.org/uniprotkb/Q14153) (Protein FAM53B):

> Acts as a regulator of Wnt signaling pathway by regulating beta-catenin (CTNNB1) nuclear localization.

**Summary**, from NCBI Gene [9679](https://www.ncbi.nlm.nih.gov/gene/9679):

> Involved in positive regulation of canonical Wnt signaling pathway. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28968](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28968) · Entrez [9679](https://www.ncbi.nlm.nih.gov/gene/9679) · UniProt [Q14153](https://www.uniprot.org/uniprotkb/Q14153) · Ensembl [ENSG00000189319](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189319)

## Data

Gene col 12115: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12115); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12115, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12115]; `tensor/DDL_lfc|DDL_z.npy` [12115]; `embed/gene_vectors.npy` [12115]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12115 or target_col == 12115). Every well: [[FAM53B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM53B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
