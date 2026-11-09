---
symbol: "RRP1"
type: "gene"
col: 8322
ensembl_id: "ENSG00000160214"
name: "ribosomal RNA processing 1"
location: "21q22.3"
module: 5
arm: "+"
pooled_cpm: 15.14
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 6
n_dd_up_clean: 28
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# RRP1

*ribosomal RNA processing 1* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (10 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 2.15× (z +12.3, q 5e-32, up in 40 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.82× (z +9.6, q 2e-19, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.779× (z -5.6, q 1e-05, down in 18 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRMT61A]] (+0.78, fdr 7e-06), [[RRS1]] (+0.77, fdr 7e-06), [[NOP16]] (+0.76, fdr 7e-06); moves opposite to [[GNAS]] (-0.65, fdr 7e-06), [[ITM2B]] (-0.56, fdr 3e-05), [[NUCB2]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8322.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.15×** | +12.3 | 5e-32 | 40/47 (Hs 766T, A498, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.82×** | +9.6 | 2e-19 | 29/47 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.68×** | +8.0 | 3e-13 | 28/45 (LoVo, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +7.9 | 4e-13 | 26/45 (CFPAC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +7.7 | 2e-12 | 26/43 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +6.6 | 4e-09 | 25/48 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +6.6 | 4e-09 | 26/46 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +6.2 | 3e-08 | 22/47 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.47×** | +6.2 | 3e-08 | 21/46 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.06×** | +6.1 | 7e-08 | 24/45 (A498, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +5.7 | 7e-07 | 20/47 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.96×** | +5.7 | 7e-07 | 19/46 (PANC-1, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +5.4 | 3e-06 | 20/42 (SNU-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +5.4 | 3e-06 | 18/46 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.39×** | +5.3 | 5e-06 | 23/48 (HOP62, HS-578T, …) | rises with dose | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.80×** | +4.9 | 3e-05 | 15/43 (A498, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.51×** | +4.7 | 8e-05 | 18/44 (SHP-77, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +4.7 | 9e-05 | 18/44 (RKO, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +4.6 | 1e-04 | 13/47 (Hs 766T, A-172, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.67×** | +4.3 | 4e-04 | 9/45 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8322.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.779×** | -5.6 | 1e-05 | 18/46 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.714×** | -5.5 | 1e-05 | 20/46 (HOP62, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.812×** | -3.8 | 0.025 | 7/48 (LoVo, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.828×** | -3.6 | 0.038 | 10/48 (MIA PaCa-2, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.808×** | -3.4 | 0.091 | 16/46 (LoVo, BT-474, …) | rises with dose | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.817×** | -3.3 | 0.092 | 9/48 (A498, KATO III, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.828× | -3.1 | 0.13 | 7/47 (LoVo, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.856× | -3.1 | 0.13 | 13/48 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.874× | -3.1 | 0.13 | 11/48 (LoVo, SW480, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8322. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 9.57 | 0 | 2 | — | [[Medroxyprogesterone acetate (drug)]] 0.05 µM 0.0661× (z -10.2) |
| [[AN3 CA (line)]] | alt | 19.0 | 0 | 1 | — | [[Ferulic acid (drug)]] 5 µM 0.0672× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 28.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 15.4 | 0 | 1 | — | [[Bergenin (drug)]] 0.05 µM 0.141× (z -9.9) |
| [[SNU-1 (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.103× (z -9.4) ⚠ toxic |
| [[SW48 (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8322), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT61A]] | +0.78 | +0.72 / +0.77 | both halves | 7e-06 | STRING 451 |
| [[RRS1]] | +0.77 | +0.68 / +0.76 | both halves | 7e-06 | same gene group; STRING 949 |
| [[NOP16]] | +0.76 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[CLUH]] | +0.72 | +0.72 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[PDCD11]] | +0.72 | +0.75 / +0.64 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 824 |
| [[SNHG17]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[EXOSC2]] | +0.71 | +0.73 / +0.69 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol |
| [[PUS1]] | +0.71 | +0.74 / +0.71 | both halves | 7e-06 | STRING 437 |
| [[LYAR]] | +0.71 | +0.70 / +0.66 | both halves | 7e-06 | STRING 731 |
| [[BYSL]] | +0.70 | +0.67 / +0.72 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 806 |
| [[NLE1]] | +0.70 | +0.67 / +0.71 | both halves | 7e-06 | STRING 755 |
| [[MYBBP1A]] | +0.69 | +0.80 / +0.64 | both halves | 7e-06 | STRING 510 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.65 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[ITM2B]] | -0.56 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[NUCB2]] | -0.56 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[TMEM59]] | -0.56 | -0.51 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises RRP1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SMARCA2]] | B | SMARCA2 activity lowers RRP1's level | lines that do not express SMARCA2 (6) vs lines expressing it (44) | 1.38× higher at baseline in the lines without SMARCA2 | 0.034 | ⚠ within organs, on part of the lines; also absent: CEMIP2, S100A13, PYROXD2 |
| [[ADD3]] | B | ADD3 activity lowers RRP1's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.29× higher at baseline in the lines without ADD3 | 0.074 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |
| [[MAP2K2]] | B | MAP2K2 activity raises RRP1's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | RRP1's natural level lowers the cells' numbers under Anethole trithione 0.5 µM (makes them more sensitive) | RRP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.491 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.613). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.4, -39.0); signed map (-2.7, -46.4). **Vector** length 83.6, 16.6% of its response variance represented; |z| ≥ 3 in 914 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.59 to 13); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.55 to 11); *ribosome biogenesis* (control, mean cos +0.54 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.0 | +12.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +6.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.0 | +8.0 |
|  | [[EX229 (drug)]] 5 µM |  | +3.7 | +4.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.6 | +9.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.5 | +6.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +4.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +1.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.1 | -5.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.0 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal RNA processing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:43,789,513-43,805,293 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NNP-1, Nop52, NOP52, RRP1A, D21S2056E |
| Gene groups (HGNC) | Ribosome biogenesis factors |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [P56182](https://www.uniprot.org/uniprotkb/P56182) (Ribosomal RNA processing protein 1 homolog A):

> Plays a critical role in the generation of 28S rRNA.

**Summary**, from NCBI Gene [8568](https://www.ncbi.nlm.nih.gov/gene/8568):

> The protein encoded by this gene is the putative homolog of the yeast ribosomal RNA processing protein RRP1. The encoded protein is involved in the late stages of nucleologenesis at the end of mitosis, and may be required for the generation of 28S rRNA. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18785](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18785) · Entrez [8568](https://www.ncbi.nlm.nih.gov/gene/8568) · UniProt [P56182](https://www.uniprot.org/uniprotkb/P56182) · Ensembl [ENSG00000160214](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160214)

## Data

Gene col 8322: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8322); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8322, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8322]; `tensor/DDL_lfc|DDL_z.npy` [8322]; `embed/gene_vectors.npy` [8322]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8322 or target_col == 8322). Every well: [[RRP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
