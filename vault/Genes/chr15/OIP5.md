---
symbol: "OIP5"
type: "gene"
col: 2421
ensembl_id: "ENSG00000104147"
name: "Opa interacting protein 5"
location: "15q15.1"
module: 67
arm: "+"
pooled_cpm: 11.57
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 20
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# OIP5

*Opa interacting protein 5* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.78× (z +7.8, q 2e-12, up in 22 of 38 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.45× (z +7.5, q 1e-11, up in 23 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.636× (z -9.0, q 9e-17, down in 26 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDCA3]] (+0.85, fdr 7e-06), [[KIF22]] (+0.84, fdr 7e-06), [[PARPBP]] (+0.83, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NDC80]] → it (grade C ⚠); 1 goes from it, the strongest it → [[NDC1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2421.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +7.8 | 2e-12 | 22/38 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +7.5 | 1e-11 | 23/45 (NCI-H1792, RKO, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.65×** | +6.8 | 2e-09 | 11/17 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +6.2 | 6e-08 | 22/43 (PANC-1, RKO, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.34×** | +5.9 | 4e-07 | 24/47 (NCI-H23, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | **1.49×** | +5.6 | 2e-06 | 19/37 (LoVo, A498, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~90% of this change | **1.33×** | +4.1 | 0.004 | 17/38 (NCI-H2030, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.35×** | +3.8 | 0.011 | 12/43 (PANC-1, J82, …) | all doses, flat | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.30×** | +3.7 | 0.014 | 19/45 (NCI-H23, H4, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.016 | 7/46 (HT-29, SK-MEL-2, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.021 | 9/46 (HT-29, NCI-H2030, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.029 | 7/45 (J82, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.074 | 9/46 (J82, SW48, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2421.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.636×** | -9.0 | 9e-17 | 26/44 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.530×** | -9.0 | 9e-17 | 29/43 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.599×** | -6.5 | 2e-08 | 23/44 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.737×** | -6.1 | 2e-07 | 25/45 (LS 180, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **0.646×** | -5.9 | 4e-07 | 21/45 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.676×** | -5.5 | 3e-06 | 19/46 (A498, SW1417, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.689×** | -5.3 | 1e-05 | 18/46 (C32, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.695×** | -5.1 | 2e-05 | 22/45 (H4, A-172, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.502×** | -5.1 | 2e-05 | 19/42 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.714×** | -4.7 | 1e-04 | 19/47 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.716×** | -4.7 | 1e-04 | 20/45 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.717×** | -4.7 | 1e-04 | 16/46 (HEC-1-A, NCI-H1573, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.799×** | -4.4 | 4e-04 | 16/46 (RKO, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.739×** | -4.2 | 9e-04 | 16/45 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.678×** | -3.9 | 0.003 | 10/47 (SW480, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.844× | -3.4 | 0.026 | 12/46 (SNU-423, CFPAC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.783×** | -3.1 | 0.062 | 11/45 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.810×** | -2.9 | 0.090 | 10/46 (NCI-H661, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **0.805×** | -2.9 | 0.094 | 10/46 (NCI-H2030, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2421. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.84 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0558× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.1000× (z -14.6) |
| [[A498 (line)]] | wt | 11.1 | 0 | 2 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0974× (z -10.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.1) |
| [[H4 (line)]] | wt | 11.9 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0575× (z -9.0) ⚠ cell-cycle shift, explains ~89% of this change |
| [[SW480 (line)]] | alt | 15.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -13.7) |
| [[A-172 (line)]] | wt | 9.59 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.158× (z -9.2) ⚠ cell-cycle shift, explains ~78% of this change |
| [[A-427 (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -13.0) ⚠ cell-cycle shift, explains ~93% of this change |
| [[COLO 205 (line)]] | alt | 9.95 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0733× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -11.5) ⚠ cell-cycle shift, explains ~93% of this change |
| [[HT-29 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.188× (z -8.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[LoVo (line)]] | wt | 8.42 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | — |
| [[LOX-IMVI (line)]] | wt | 8.56 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.225× (z -10.1) ⚠ cell-cycle shift, explains ~86% of this change |
| [[LS 180 (line)]] | wt | 9.18 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.138× (z -12.6) ⚠ cell-cycle shift, explains ~86% of this change |
| [[MIA PaCa-2 (line)]] | alt | 9.23 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0607× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 12.6 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.109× (z -8.7) |
| [[A549 (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2421), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDCA3]] | +0.85 | +0.85 / +0.83 | both halves | 7e-06 | STRING 671 |
| [[KIF22]] | +0.84 | +0.82 / +0.82 | both halves | 7e-06 |  |
| [[PARPBP]] | +0.83 | +0.85 / +0.82 | both halves | 7e-06 | STRING 559 |
| [[KIF18B]] | +0.83 | +0.86 / +0.79 | both halves | 7e-06 |  |
| [[DTYMK]] | +0.82 | +0.76 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[SPC25]] | +0.82 | +0.83 / +0.78 | both halves | 7e-06 | STRING 791 |
| [[PBK]] | +0.81 | +0.81 / +0.81 | both halves | 7e-06 | STRING 854 |
| [[TACC3]] | +0.81 | +0.80 / +0.78 | both halves | 7e-06 | STRING 445 |
| [[CDC25C]] | +0.81 | +0.79 / +0.80 | both halves | 7e-06 | STRING 573 |
| [[CDCA8]] | +0.81 | +0.80 / +0.78 | both halves | 7e-06 | STRING 856 |
| [[AURKB]] | +0.80 | +0.81 / +0.77 | both halves | 7e-06 | STRING 660 |
| [[SPAG5]] | +0.80 | +0.76 / +0.77 | both halves | 7e-06 | STRING 574 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDC80]] | C | NDC80 activity raises OIP5's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.31× lower at baseline in the lines without NDC80 | 0.055 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDC1]] | C | OIP5's natural level strengthens NDC1's drug response | OIP5's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.03; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.879). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-34.9, -53.7); signed map (-46.8, -41.1). **Vector** length 101, 23.4% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.77 to 12); *G2/M checkpoint* (hallmark, mean cos +0.77 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.73 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.4 | +3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | +4.0 | +3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +7.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.4 | +2.9 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +3.1 | +5.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.0 | +3.8 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.0 | +3.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.8 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -9.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | -4.6 | -5.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | -4.4 | -6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -9.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.6 | -5.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -4.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | Opa interacting protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:41,309,273-41,332,591 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MIS18B, hMIS18beta, CT86 |
| Reactome | 4 pathways, smallest: Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly; Chromosome Maintenance |
| Matched by | ensembl_id |

**Function**, from UniProt [O43482](https://www.uniprot.org/uniprotkb/O43482) (Protein Mis18-beta):

> Required for recruitment of CENPA to centromeres and normal chromosome segregation during mitosis.

**Summary**, from NCBI Gene [11339](https://www.ncbi.nlm.nih.gov/gene/11339):

> The protein encoded by this gene localizes to centromeres, where it is essential for recruitment of CENP-A through the mediator Holliday junction recognition protein. Expression of this gene is upregulated in several cancers, making it a putative therapeutic target. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:20300](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20300) · Entrez [11339](https://www.ncbi.nlm.nih.gov/gene/11339) · UniProt [O43482](https://www.uniprot.org/uniprotkb/O43482) · Ensembl [ENSG00000104147](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104147)

## Data

Gene col 2421: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2421); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2421, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2421]; `tensor/DDL_lfc|DDL_z.npy` [2421]; `embed/gene_vectors.npy` [2421]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2421 or target_col == 2421). Every well: [[OIP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OIP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
