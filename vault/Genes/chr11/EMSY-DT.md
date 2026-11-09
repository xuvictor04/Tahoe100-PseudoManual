---
symbol: "EMSY-DT"
type: "gene"
col: 14919
ensembl_id: "ENSG00000255135"
name: "EMSY divergent transcript"
location: "11q13.5"
module: 35
arm: "+"
pooled_cpm: 2.86
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# EMSY-DT

*EMSY divergent transcript* — 11q13.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.34× (z +21.0, q 0e+00, up in 32 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.656× (z -3.8, q 0.089, down in 13 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (KATO III 0.117×); [[Rifaximin (drug)]] 5 µM in 1 line (LS 180 0.0602×); [[Rapamycin (drug)]] 5 µM in 1 line (A498 0.0956×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAXBP1-AS1]] (+0.70, fdr 1e-05), [[LINC00938]] (+0.69, fdr 3e-05), [[SPEN-AS1]] (+0.69, fdr 7e-06); moves opposite to [[NAPG]] (-0.60, fdr 5e-05), [[HERC2]] (-0.58, fdr 5e-05), [[RSU1]] (-0.58, fdr 5e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14919.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.34×** | +21.0 | 0e+00 | 32/32 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.30×** | +10.2 | 6e-22 | 1/1 (PANC-1) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.11×** | +9.3 | 2e-18 | 1/1 (PANC-1) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.63×** | +8.3 | 2e-14 | 15/27 (HS-578T, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.44×** | +7.9 | 3e-13 | 15/17 (KATO III, HEC-1-A, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.85×** | +7.7 | 1e-12 | 17/46 (NCI-H2030, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +6.9 | 5e-10 | 21/37 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.73×** | +6.9 | 5e-10 | 16/35 (A-172, NCI-H2030, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.06×** | +6.4 | 9e-09 | 11/16 (NCI-H2030, SHP-77, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +5.8 | 5e-07 | 5/17 (J82, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.4 | 4e-06 | 12/45 (PANC-1, BT-474, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.64×** | +4.4 | 6e-04 | 6/33 (LoVo, A-172, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.61×** | +4.0 | 0.002 | 11/42 (MIA PaCa-2, A-172, …) | all doses, flat | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +3.9 | 0.003 | 16/41 (HCT15, RKO, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +3.9 | 0.004 | 11/45 (A-172, KATO III, …) | all doses, flat | cell-cycle shift (explains ~17% here); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.52×** | +3.4 | 0.020 | 6/28 (RPMI-7951, NCI-H2030, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +3.1 | 0.058 | 6/47 (HS-578T, J82, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +3.0 | 0.076 | 1/42 (SNU-423) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +2.9 | 0.095 | 6/42 (A-172, SHP-77, …) | all doses, stronger at high dose | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **1.26×** | +2.9 | 0.099 | 5/44 (SW480, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14919.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (KATO III 0.117×); [[Rifaximin (drug)]] 5 µM in 1 line (LS 180 0.0602×); [[Rapamycin (drug)]] 5 µM in 1 line (A498 0.0956×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.656×** | -3.8 | 0.089 | 13/45 (KATO III, A549, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.653×** | -3.6 | 0.089 | 11/40 (SW480, H4, …) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 5 µM |  | 0.685× | -3.3 | 0.21 | 8/39 (LS 180, HT-29, …) | top dose only | position effect removed |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.701× | -3.1 | 0.31 | 8/41 (SHP-77, A498, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14919. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.43× (z +8.7) | — |
| [[A498 (line)]] | wt | 1.12 | 0 | 1 | — | [[Rapamycin (drug)]] 5 µM 0.0956× (z -8.5) |
| [[HOP62 (line)]] | alt | 1.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 2.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +8.6) | — |
| [[KATO III (line)]] | alt | 8.09 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.117× (z -9.3) |
| [[LS 180 (line)]] | wt | 3.33 | 0 | 1 | — | [[Rifaximin (drug)]] 5 µM 0.0602× (z -8.7) |
| [[PANC-1 (line)]] | alt | 2.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.11× (z +10.8) | — |
| [[A-427 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.858 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14919), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAXBP1-AS1]] | +0.70 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[LINC00938]] | +0.69 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[SPEN-AS1]] | +0.69 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[C11orf71]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[TTC32]] | +0.69 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[ZBED5-AS1]] | +0.68 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[UPK2]] | +0.67 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[PIGP]] | +0.66 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[MALINC1]] | +0.66 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[PNISR-AS1]] | +0.66 | +0.72 / +0.37 | both halves | 7e-05 |  |
| [[PSMD14-DT]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 | same gene group |
| [[HSDL2-AS1]] | +0.65 | +0.67 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAPG]] | -0.60 | -0.69 / -0.40 | both halves | 5e-05 |  |
| [[HERC2]] | -0.58 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[RSU1]] | -0.58 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[USP14]] | -0.57 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[ERI3]] | -0.57 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[SLC23A2]] | -0.56 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[HERC2P2]] | -0.56 | -0.45 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EMSY-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises EMSY-DT's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.674). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (1.5, 18.3); signed map (25.2, -13.9). **Vector** length 46.9, 5.82% of its response variance represented; |z| ≥ 3 in 917 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +21.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +7.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +8.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +5.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +1.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.6 | -3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.1 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +2.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | +0.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -0.9 | -0.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | EMSY divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q13.5 — chr11:76,435,559-76,444,690 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55507](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55507) · Entrez [124902718](https://www.ncbi.nlm.nih.gov/gene/124902718) · Ensembl [ENSG00000255135](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255135)

## Data

Gene col 14919: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14919); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14919, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14919]; `tensor/DDL_lfc|DDL_z.npy` [14919]; `embed/gene_vectors.npy` [14919]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14919 or target_col == 14919). Every well: [[EMSY-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EMSY-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
