---
symbol: "PUS1"
type: "gene"
col: 10802
ensembl_id: "ENSG00000177192"
name: "pseudouridine synthase 1"
location: "12q24.33"
module: 5
arm: "+"
pooled_cpm: 16.83
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 2
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PUS1

*pseudouridine synthase 1* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (12 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 2.95× (z +15.2, q 0e+00, up in 46 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.73× (z +7.6, q 4e-12, up in 32 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.548× (z -4.4, q 0.004, down in 17 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.564×; ⚠ position not correctable); [[Simotinib (drug)]] 5 µM in 1 line (AsPC-1 0.121×; ⚠ toxic); [[Ivermectin (drug)]] 0.5 µM in 1 line (COLO 205 0.0768×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR4]] (+0.93, fdr 7e-06), [[NOP16]] (+0.82, fdr 7e-06), [[LETM1]] (+0.82, fdr 7e-06); moves opposite to [[TMEM59]] (-0.66, fdr 7e-06), [[USP33]] (-0.65, fdr 7e-06), [[ARL6IP5]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10802.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.95×** | +15.2 | 0e+00 | 46/47 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +10.1 | 1e-21 | 36/43 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +7.6 | 4e-12 | 32/46 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.32×** | +6.2 | 1e-07 | 29/45 (PANC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.59×** | +6.0 | 2e-07 | 16/31 (A549, NCI-H2347, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.50×** | +5.7 | 1e-06 | 23/47 (SHP-77, SW480, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[TAK-733 (drug)]] 5 µM |  | **2.08×** | +5.4 | 6e-06 | 26/45 (A498, PANC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +5.0 | 3e-05 | 24/47 (H4, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.0 | 3e-05 | 2/48 (KATO III, AsPC-1) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +5.0 | 4e-05 | 18/43 (SNU-423, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.95×** | +4.9 | 5e-05 | 20/45 (PANC-1, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.95×** | +4.9 | 5e-05 | 19/42 (PANC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.41×** | +4.8 | 8e-05 | 22/47 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +4.8 | 8e-05 | 19/45 (RKO, NCI-H2347, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.40×** | +4.7 | 9e-05 | 18/47 (HOP62, SNU-423, …) | rises with dose | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.87×** | +4.6 | 1e-04 | 22/44 (A549, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +4.2 | 7e-04 | 18/46 (AsPC-1, SNU-423, …) | rises with dose | position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.52×** | +4.2 | 8e-04 | 14/46 (NCI-H460, HT-29, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.2 | 8e-04 | 13/48 (NCI-H2347, Panc 03.27, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 1e-03 | 16/45 (MIA PaCa-2, NCI-H460, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.003 | 19/47 (NCI-H460, NCI-H1573, …) | two highest doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.003 | 6/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10802.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.564×; ⚠ position not correctable); [[Simotinib (drug)]] 5 µM in 1 line (AsPC-1 0.121×; ⚠ toxic); [[Ivermectin (drug)]] 0.5 µM in 1 line (COLO 205 0.0768×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.548×** | -4.4 | 0.004 | 17/44 (SW48, RKO, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.726×** | -4.4 | 0.004 | 19/46 (HepG2/C3A, C32, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.783× | -3.3 | 0.13 | 13/46 (A498, SW1417, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.849× | -3.3 | 0.13 | 13/48 (A498, RKO, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.829× | -3.2 | 0.14 | 12/48 (MIA PaCa-2, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Methotrexate (drug)]] 0.5 µM |  | 0.801× | -3.1 | 0.16 | 8/47 (HepG2/C3A, NCI-H2347, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.839× | -3.0 | 0.20 | 13/48 (LoVo, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10802. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 18.8 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.78× (z +8.5) ⚠ unreliable plate only | — |
| [[AsPC-1 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.121× (z -9.5) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 9.22 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.0768× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.564× (z -11.8) ⚠ position not correctable |
| [[NCI-H460 (line)]] | wt | 24.3 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.84× (z +10.4) ⚠ unreliable plate only | — |
| [[RKO (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -8.5) ⚠ cell-cycle shift, explains ~78% of this change |
| [[A-172 (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10802), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR4]] | +0.93 | +0.92 / +0.92 | both halves | 7e-06 | pathway: tRNA modification in the nucleus and cytosol; STRING 910 |
| [[NOP16]] | +0.82 | +0.86 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[LETM1]] | +0.82 | +0.78 / +0.82 | both halves | 7e-06 |  |
| [[ARMC6]] | +0.81 | +0.80 / +0.77 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.80 | +0.78 / +0.82 | both halves | 7e-06 | STRING 455 |
| [[PPRC1]] | +0.80 | +0.84 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[GNL3L]] | +0.79 | +0.85 / +0.76 | both halves | 7e-06 |  |
| [[PNO1]] | +0.79 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[PUM3]] | +0.78 | +0.83 / +0.73 | both halves | 7e-06 |  |
| [[NOP2]] | +0.78 | +0.78 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING; STRING 723 |
| [[DDX21]] | +0.78 | +0.80 / +0.74 | both halves | 7e-06 |  |
| [[URB2]] | +0.78 | +0.75 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM59]] | -0.66 | -0.68 / -0.71 | both halves | 7e-06 |  |
| [[USP33]] | -0.65 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[ARL6IP5]] | -0.64 | -0.63 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.901). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.7, -35.9); signed map (-1.5, -47.0). **Vector** length 106, 24.9% of its response variance represented; |z| ≥ 3 in 1,044 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.65 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.66 to 19); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.67 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.5 | +15.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +10.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.8 | +6.2 |
|  | [[EX229 (drug)]] 5 µM |  | +4.7 | +4.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.3 | +5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.5 | +4.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -2.9 | -3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | -4.4 |
|  | [[NG25 (drug)]] 5 µM |  | -2.8 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.7 | -2.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.5 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | pseudouridine synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:131,929,200-131,945,896 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MLASA1 |
| Gene groups (HGNC) | Pseudouridine synthases |
| Hallmark sets | MYC_TARGETS_V2, IL2_STAT5_SIGNALING |
| Reactome | 4 pathways, smallest: tRNA modification in the mitochondrion; tRNA modification in the nucleus and cytosol; tRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y606](https://www.uniprot.org/uniprotkb/Q9Y606) (Pseudouridylate synthase 1 homolog):

> Pseudouridylate synthase that catalyzes pseudouridylation of tRNAs and mRNAs. Acts on positions 27/28 in the anticodon stem and also positions 34 and 36 in the anticodon of an intron containing tRNA. Also catalyzes pseudouridylation of mRNAs: mediates pseudouridylation of mRNAs with the consensus sequence 5'-UGUAG-3'. Acts as a regulator of pre-mRNA splicing by mediating pseudouridylation of pre-mRNAs at locations associated with alternatively spliced regions. Pseudouridylation of pre-mRNAs …

**Summary**, from NCBI Gene [80324](https://www.ncbi.nlm.nih.gov/gene/80324):

> This gene encodes a pseudouridine synthase that converts uridine to pseudouridine once it has been incorporated into an RNA molecule. The encoded enzyme may play an essential role in tRNA function and in stabilizing the secondary and tertiary structure of many RNAs. A mutation in this gene has been linked to mitochondrial myopathy and sideroblastic anemia. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:15508](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15508) · Entrez [80324](https://www.ncbi.nlm.nih.gov/gene/80324) · UniProt [Q9Y606](https://www.uniprot.org/uniprotkb/Q9Y606) · Ensembl [ENSG00000177192](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177192)

## Data

Gene col 10802: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10802); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10802, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10802]; `tensor/DDL_lfc|DDL_z.npy` [10802]; `embed/gene_vectors.npy` [10802]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10802 or target_col == 10802). Every well: [[PUS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PUS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
