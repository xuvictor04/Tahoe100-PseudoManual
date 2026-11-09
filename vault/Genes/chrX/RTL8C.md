---
symbol: "RTL8C"
type: "gene"
col: 5581
ensembl_id: "ENSG00000134590"
name: "retrotransposon Gag like 8C"
location: "Xq26.3"
module: 50
arm: "+"
pooled_cpm: 14.88
n_lines_expressing: 41
n_dd_up: 3
n_dd_down: 11
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# RTL8C

*retrotransposon Gag like 8C* — Xq26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.69× (z +5.7, q 7e-06, up in 18 of 31 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.26× (z +3.5, q 0.094, up in 18 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (MIA PaCa-2 5.86×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.491× (z -10.7, q 5e-24, down in 29 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BSG]] (+0.69, fdr 7e-06), [[TRAPPC1]] (+0.69, fdr 7e-06), [[CHPF]] (+0.65, fdr 7e-06); moves opposite to [[GSTO2]] (-0.54, fdr 5e-05), [[TATDN1]] (-0.52, fdr 2e-05), [[GCFC2]] (-0.51, fdr 4e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CPEB1]] → it (grade B ⚠); 2 go from it, the strongest it → [[GM2A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5581.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (MIA PaCa-2 5.86×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.69×** | +5.7 | 7e-06 | 18/31 (SNU-423, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +5.5 | 1e-05 | 15/23 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.094 | 18/37 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | 1.24× | +3.2 | 0.20 | 16/39 (A-427, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.35× | +3.1 | 0.21 | 15/33 (NCI-H1573, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5581.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.491×** | -10.7 | 5e-24 | 29/38 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.493×** | -7.7 | 5e-12 | 27/37 (SK-MEL-2, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.497×** | -7.2 | 2e-10 | 29/39 (hTERT-HPNE, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.516×** | -6.9 | 8e-10 | 30/38 (H4, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.637×** | -4.9 | 1e-04 | 25/39 (hTERT-HPNE, J82, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.659×** | -4.3 | 0.001 | 19/37 (SNU-423, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.700×** | -3.9 | 0.009 | 19/37 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.541×** | -3.5 | 0.034 | 12/29 (A498, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.732×** | -3.4 | 0.047 | 17/39 (H4, NCI-H661, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.738×** | -3.3 | 0.057 | 13/38 (H4, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.740×** | -3.3 | 0.058 | 15/39 (SK-MEL-2, hTERT-HPNE, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.756× | -3.0 | 0.11 | 9/38 (Hs 766T, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.757× | -3.0 | 0.11 | 14/39 (LS 180, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5581. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 27.8 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0477× (z -14.6) |
| [[SK-MEL-2 (line)]] | alt | 31.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -9.0) |
| [[A-172 (line)]] | wt | 16.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 19.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -10.0) |
| [[HOP62 (line)]] | alt | 26.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 13.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.86× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 39.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -14.2) |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -13.9) |
| [[SNU-423 (line)]] | alt | 36.8 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.270× (z -9.6) |
| [[A-427 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.775 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.877 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.15 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.994 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.784 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.862 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.715 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5581), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BSG]] | +0.69 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[TRAPPC1]] | +0.69 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[CHPF]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[ECM1]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[NAGA]] | +0.64 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[AP2M1]] | +0.62 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[GLT8D1]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[SPARC]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[CERCAM]] | +0.59 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[SMPD1]] | +0.58 | +0.34 / +0.66 | both halves | 1e-04 |  |
| [[ARSA]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PCYOX1]] | +0.58 | +0.59 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSTO2]] | -0.54 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[TATDN1]] | -0.52 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[GCFC2]] | -0.51 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[DNAJC2]] | -0.49 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[CPEB1]] | -0.48 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[THOC2]] | -0.48 | -0.52 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CPEB1]] | B | CPEB1 activity raises RTL8C's level | lines that do not express CPEB1 (24) vs lines expressing it (26) | 3.26× lower at baseline in the lines without CPEB1 | 0.060 | ⚠ within organs, on part of the lines; also absent: GLIS1, COLEC12, TUB |
| [[PSMB5]] | B | PSMB5 activity raises RTL8C's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GM2A]] | B | RTL8C activity raises GM2A's level | lines that do not express RTL8C (9) vs lines expressing it (41) | 1.75× lower at baseline in the lines without RTL8C | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000286964, RTL8A, EHD3; its own permutation p |
| [[RTL8A]] | C | RTL8C activity raises RTL8A's level | lines that do not express RTL8C (9) vs lines expressing it (41) | 5.64× lower at baseline in the lines without RTL8C | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000286964, RTL8A, EHD3; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.0, -21.0); signed map (-53.4, -11.8). **Vector** length 75.1, 17.0% of its response variance represented; |z| ≥ 3 in 619 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *epithelial mesenchymal transition* (hallmark, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +1.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +0.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.5 | +0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.4 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -7.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.2 | -4.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.0 | -6.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.0 | -7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.9 | -10.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -3.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.7 | -1.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | retrotransposon Gag like 8C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.3 — chrX:135,032,355-135,033,546 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Mart8, Mar8, MAR8C, SIRH5; previously CXX1, FAM127A |
| Gene groups (HGNC) | Retrotransposon Gag like family |
| Matched by | ensembl_id |

UniProt [A6ZKI3](https://www.uniprot.org/uniprotkb/A6ZKI3) carries no function annotation.

**Summary**, from NCBI Gene [8933](https://www.ncbi.nlm.nih.gov/gene/8933):

> Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:2569](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2569) · Entrez [8933](https://www.ncbi.nlm.nih.gov/gene/8933) · UniProt [A6ZKI3](https://www.uniprot.org/uniprotkb/A6ZKI3) · Ensembl [ENSG00000134590](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134590)

## Data

Gene col 5581: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5581); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5581, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5581]; `tensor/DDL_lfc|DDL_z.npy` [5581]; `embed/gene_vectors.npy` [5581]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5581 or target_col == 5581). Every well: [[RTL8C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTL8C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
