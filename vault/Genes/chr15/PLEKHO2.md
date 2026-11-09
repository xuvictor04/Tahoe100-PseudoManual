---
symbol: "PLEKHO2"
type: "gene"
col: 14288
ensembl_id: "ENSG00000241839"
name: "pleckstrin homology domain containing O2"
location: "15q22.31"
module: 162
arm: "+"
pooled_cpm: 9.6
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# PLEKHO2

*pleckstrin homology domain containing O2* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.95× (z +16.6, q 0e+00, up in 37 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.626× (z -5.1, q 2e-04, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.0907×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW1417 0.0859×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Erlotinib (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0735×); [[Atazanavir (sulfate) (drug)]] 0.5 µM in 1 line (A-427 0.0890×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RPMI-7951 0.172×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCORL1]] (+0.64, fdr 7e-06), [[SLC9A3R1]] (+0.63, fdr 1e-05), [[EPHB3]] (+0.63, fdr 1e-05); moves opposite to [[QRSL1]] (-0.60, fdr 2e-05), [[ITFG1]] (-0.56, fdr 1e-05), [[FBXO9]] (-0.56, fdr 5e-05).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SOCS3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14288.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.95×** | +16.6 | 0e+00 | 37/44 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.88×** | +11.5 | 3e-28 | 40/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.41×** | +9.6 | 2e-19 | 39/47 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.26×** | +8.9 | 9e-17 | 40/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.76×** | +5.9 | 3e-07 | 25/46 (A498, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +5.9 | 3e-07 | 25/44 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +5.0 | 6e-05 | 24/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +4.1 | 0.002 | 15/42 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.003 | 19/47 (HT-29, SW1417, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +3.5 | 0.030 | 15/43 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.036 | 21/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.039 | 11/45 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.053 | 13/44 (SNU-423, HT-29, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14288.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.0907×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW1417 0.0859×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Erlotinib (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0735×); [[Atazanavir (sulfate) (drug)]] 0.5 µM in 1 line (A-427 0.0890×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RPMI-7951 0.172×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.626×** | -5.1 | 2e-04 | 23/48 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -3.8 | 0.048 | 14/41 (RPMI-7951, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.802× | -3.3 | 0.16 | 15/47 (SW480, RKO, …) | all doses, flat | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.732× | -3.3 | 0.16 | 19/41 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.777× | -3.2 | 0.16 | 13/47 (SW480, NCI-H1573, …) | all doses, flat | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14288. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 6.84 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.23× (z +14.7) | — |
| [[hTERT-HPNE (line)]] | wt | 15.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.65× (z +10.6) | [[Erlotinib (drug)]] 5 µM 0.0735× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 8.70 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +8.9) | [[Docetaxel (drug)]] 0.05 µM 0.114× (z -9.2) ⚠ transcription drop |
| [[RPMI-7951 (line)]] | alt | 26.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +10.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -9.1) |
| [[SNU-423 (line)]] | alt | 12.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +12.4) | [[XRK3F2 (drug)]] 0.5 µM 0.0842× (z -9.0) |
| [[SW 900 (line)]] | alt | 7.44 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.0853× (z -8.8) |
| [[A-172 (line)]] | wt | 14.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +9.5) | — |
| [[A-427 (line)]] | wt | 4.43 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0890× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 8.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +9.9) | — |
| [[C32 (line)]] | wt | 22.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 12.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +13.1) | — |
| [[HCT15 (line)]] | alt | 9.93 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0851× (z -8.5) |
| [[HOP62 (line)]] | alt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +12.3) | — |
| [[HS-578T (line)]] | alt | 5.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.94× (z +11.3) | — |
| [[J82 (line)]] | alt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +10.9) | — |
| [[LOX-IMVI (line)]] | wt | 13.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0907× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 4.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +11.3) | — |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0907× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~81% of this change |
| [[PANC-1 (line)]] | alt | 8.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +9.0) | — |
| [[SK-MEL-2 (line)]] | alt | 28.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +12.0) | — |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0859× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14288), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCORL1]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[SLC9A3R1]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[EPHB3]] | +0.63 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[NCKAP5L]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[IER2]] | +0.61 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[SEMA3F]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[BAIAP3]] | +0.60 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[PLK3]] | +0.60 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[DUSP2]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[EPPK1]] | +0.59 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[NOTCH1]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[SYT5]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QRSL1]] | -0.60 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[ITFG1]] | -0.56 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[FBXO9]] | -0.56 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[ZNF148]] | -0.54 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[TRAPPC13]] | -0.54 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[GTF2I]] | -0.53 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[PCMTD1-DT]] | -0.52 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[GPALPP1]] | -0.52 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[ANKRD13C]] | -0.52 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[ANGEL2]] | -0.51 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[FAM120C]] | -0.51 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[PIK3R4]] | -0.51 | -0.61 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOCS3]] | B | SOCS3 activity raises PLEKHO2's level | lines that do not express SOCS3 (6) vs lines expressing it (44) | 1.66× lower at baseline in the lines without SOCS3 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with PIK3CA, ZFHX3, ACVR2A; also absent: LARP6, PTPRH, ZNF284; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.734). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.7, -6.2); signed map (-2.1, 25.9). **Vector** length 85.5, 16.7% of its response variance represented; |z| ≥ 3 in 1,057 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *estrogen response late* (hallmark, mean cos +0.52 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +16.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.6 | +11.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.2 | +9.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +2.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +2.4 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -3.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -3.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | +0.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | -5.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology domain containing O2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:64,841,883-64,868,002 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761K2312, PP1628, pp9099; previously PLEKHQ1 |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

UniProt [Q8TD55](https://www.uniprot.org/uniprotkb/Q8TD55) carries no function annotation.

**Summary**, from NCBI Gene [80301](https://www.ncbi.nlm.nih.gov/gene/80301):

> Predicted to be involved in macrophage apoptotic process. Predicted to be located in extracellular region and ficolin-1-rich granule lumen. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30026](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30026) · Entrez [80301](https://www.ncbi.nlm.nih.gov/gene/80301) · UniProt [Q8TD55](https://www.uniprot.org/uniprotkb/Q8TD55) · Ensembl [ENSG00000241839](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241839)

## Data

Gene col 14288: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14288); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14288, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14288]; `tensor/DDL_lfc|DDL_z.npy` [14288]; `embed/gene_vectors.npy` [14288]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14288 or target_col == 14288). Every well: [[PLEKHO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
