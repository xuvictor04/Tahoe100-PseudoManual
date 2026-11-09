---
symbol: "TWNK"
type: "gene"
col: 2882
ensembl_id: "ENSG00000107815"
name: "twinkle mtDNA helicase"
location: "10q24.31"
module: 5
arm: "+"
pooled_cpm: 10.88
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TWNK

*twinkle mtDNA helicase* — 10q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (12 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.60× (z +10.8, q 2e-24, up in 31 of 37 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 2.14× (z +9.0, q 1e-16, up in 33 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (RKO 0.169×, SW480 0.305×, PANC-1 0.423×, SW48 0.205×; ⚠ cell-cycle shift, explains ~0% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (RKO 0.0814×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.251×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Imiquimod (maleate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0912×); [[Cytarabine (drug)]] 5 µM in 1 line (HT-29 0.0573×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BYSL]] (+0.84, fdr 7e-06), [[NOP16]] (+0.84, fdr 7e-06), [[WDR4]] (+0.80, fdr 7e-06); moves opposite to [[MPC2]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LTBR]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Belzutifan (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2882.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.60×** | +10.8 | 2e-24 | 31/37 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.14×** | +9.0 | 1e-16 | 33/47 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.21×** | +8.6 | 2e-15 | 18/23 (NCI-H460, SW1417, …) | inconsistent across doses | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +8.3 | 1e-14 | 29/42 (NCI-H1792, HT-29, …) | top dose only | cell-cycle shift (explains ~23% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **3.73×** | +8.1 | 7e-14 | 33/43 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.95×** | +7.8 | 4e-13 | 25/47 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +7.8 | 4e-13 | 24/43 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.46×** | +7.6 | 2e-12 | 34/46 (SHP-77, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +7.3 | 2e-11 | 27/45 (NCI-H460, SW480, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.83×** | +7.1 | 7e-11 | 29/45 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.83×** | +7.1 | 7e-11 | 27/46 (NCI-H1573, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +7.0 | 1e-10 | 31/47 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.74×** | +6.5 | 3e-09 | 29/47 (Panc 03.27, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.75×** | +6.1 | 4e-08 | 27/44 (PANC-1, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.64×** | +5.8 | 3e-07 | 21/45 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +4.9 | 3e-05 | 18/45 (NCI-H2347, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.52×** | +4.7 | 7e-05 | 22/45 (COLO 205, NCI-H1792, …) | top dose only | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.47×** | +4.5 | 2e-04 | 15/46 (Panc 03.27, NCI-H460, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.43×** | +3.9 | 0.002 | 13/45 (HEC-1-A, AN3 CA, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2882.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (RKO 0.169×, SW480 0.305×, PANC-1 0.423×, SW48 0.205×; ⚠ cell-cycle shift, explains ~0% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (RKO 0.0814×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.251×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Imiquimod (maleate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0912×); [[Cytarabine (drug)]] 5 µM in 1 line (HT-29 0.0573×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.790× | -3.4 | 0.19 | 13/47 (LoVo, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.744× | -3.4 | 0.19 | 15/46 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.822× | -3.3 | 0.19 | 11/47 (A-427, LS 180, …) | rises with dose | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.767× | -3.1 | 0.20 | 11/46 (SK-MEL-2, SW480, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.779× | -3.0 | 0.20 | 10/47 (A-427, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.760× | -3.0 | 0.20 | 14/47 (LoVo, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.776× | -3.0 | 0.20 | 11/47 (LOX-IMVI, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2882. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 22.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 27.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0814× (z -13.3) |
| [[SW48 (line)]] | wt | 21.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.77 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.0715× (z -9.8) |
| [[A-427 (line)]] | wt | 16.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -9.0) |
| [[C-33 A (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.166× (z -8.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 4.34 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 11.0× (z +8.6) ⚠ toxic | — |
| [[HepG2_C3A (line)]] | wt | 9.96 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0912× (z -10.5) |
| [[HT-29 (line)]] | alt | 5.68 | 0 | 1 | — | [[Cytarabine (drug)]] 5 µM 0.0573× (z -9.8) |
| [[LS 180 (line)]] | wt | 7.59 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0764× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.576× (z -9.8) ⚠ position not correctable |
| [[NCI-H2030 (line)]] | alt | 10.7 | 0 | 1 | — | [[Neratinib (drug)]] 0.05 µM 0.172× (z -9.8) |
| [[SW480 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2882), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BYSL]] | +0.84 | +0.88 / +0.79 | both halves | 7e-06 |  |
| [[NOP16]] | +0.84 | +0.86 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[WDR4]] | +0.80 | +0.86 / +0.74 | both halves | 7e-06 |  |
| [[MRTO4]] | +0.80 | +0.82 / +0.77 | both halves | 7e-06 |  |
| [[NOP2]] | +0.79 | +0.81 / +0.74 | both halves | 7e-06 |  |
| [[GRWD1]] | +0.79 | +0.84 / +0.73 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.77 | +0.87 / +0.67 | both halves | 7e-06 |  |
| [[PUS1]] | +0.77 | +0.81 / +0.73 | both halves | 7e-06 | STRING 414 |
| [[TSR1]] | +0.76 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[DHX33]] | +0.76 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[LSG1]] | +0.75 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[URB2]] | +0.75 | +0.78 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPC2]] | -0.61 | -0.64 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LTBR]] | B | LTBR activity lowers TWNK's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.45× higher at baseline in the lines without LTBR | 0.087 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Belzutifan (drug)]] 5 µM | C | TWNK's natural level raises the cells' numbers under Belzutifan 5 µM (protects the cells) | TWNK's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.60 | 0.469 over the table, 0.076 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.850). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.7, -36.6); signed map (-2.0, -46.9). **Vector** length 108, 26.7% of its response variance represented; |z| ≥ 3 in 1,163 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.71 to 13); *rRNA processing* (reactome, mean cos +0.63 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.63 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +5.9 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +7.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.0 | +10.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +7.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +4.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.0 | +3.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.1 | -0.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.1 | -2.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.5 | -3.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.4 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | twinkle mtDNA helicase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.31 — chr10:100,987,367-100,994,403 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PEO, PEO1, TWINKLE, FLJ21832, TWINL; previously IOSCA, C10orf2 |
| Gene groups (HGNC) | Helicases; Mitochondrial nucleoid associated proteins |
| Reactome | 6 pathways, smallest: Strand-asynchronous mitochondrial DNA replication; Transcriptional activation of mitochondrial biogenesis; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RR1](https://www.uniprot.org/uniprotkb/Q96RR1) (Twinkle mtDNA helicase):

> [Isoform 1]: Mitochondrial helicase involved in mtDNA replication and repair. Might have a role in mtDNA repair. Has DNA strand separation activity needed to form a processive replication fork for leading strand synthesis which is catalyzed by the formation of a replisome complex with POLG and mtSDB. Preferentially unwinds DNA substrates with pre-existing 5'-and 3'- single-stranded tails but is also active on a 5'- flap substrate. Can dissociate the invading strand of immobile or mobile D-loop …

**Summary**, from NCBI Gene [56652](https://www.ncbi.nlm.nih.gov/gene/56652):

> This gene encodes a hexameric DNA helicase which unwinds short stretches of double-stranded DNA in the 5' to 3' direction and, along with mitochondrial single-stranded DNA binding protein and mtDNA polymerase gamma, is thought to play a key role in mtDNA replication. The protein localizes to the mitochondrial matrix and mitochondrial nucleoids. Mutations in this gene cause infantile onset spinocerebellar ataxia (IOSCA) and progressive external ophthalmoplegia (PEO) and are also associated with …

**Accessions** — [HGNC:1160](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1160) · Entrez [56652](https://www.ncbi.nlm.nih.gov/gene/56652) · UniProt [Q96RR1](https://www.uniprot.org/uniprotkb/Q96RR1) · Ensembl [ENSG00000107815](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107815)

## Data

Gene col 2882: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2882); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2882, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2882]; `tensor/DDL_lfc|DDL_z.npy` [2882]; `embed/gene_vectors.npy` [2882]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2882 or target_col == 2882). Every well: [[TWNK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TWNK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
