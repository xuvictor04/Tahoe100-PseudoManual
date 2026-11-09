---
symbol: "IMPA1P1"
type: "gene"
col: 14771
ensembl_id: "ENSG00000251521"
name: "inositol monophosphatase 1 pseudogene 1"
location: "8q21.13"
module: 39
arm: "+"
pooled_cpm: 3.11
n_lines_expressing: 44
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 7
direction_downstream: 23
tags: ["gene", "module/039", "written"]
generated_by: "tahoemap"
---

# IMPA1P1

*inositol monophosphatase 1 pseudogene 1* — 8q21.13

> [!summary] In one line
> IMPA1P1 is a transcribed pseudogene of inositol monophosphatase 1, with no known function of its own.

## What it is

The record is almost entirely annotation. IMPA1P1 lies on chromosome 8 near its parent gene IMPA1 and is classed as a transcribed unprocessed pseudogene with a single non-coding transcript. The parent enzyme is well characterised — IMPA1 recycles free inositol by dephosphorylating myo-inositol monophosphate, and is the classical candidate target of lithium — but none of that transfers to a pseudogene not expected to make protein. No function, pathway, partner or phenotype has been assigned to IMPA1P1, and no regulatory role of the kind shown for some other transcribed pseudogenes. What is attached to it is statistical: copy-number variants, and association signals in its interval more plausibly read as tagging IMPA1, which sits about 30 kb 5′ of it on the same strand.

## What is uncertain

The first question is whether the measurement means anything. A pseudogene retaining high identity to a well-expressed parent is exactly where short reads cannot be assigned confidently, so the apparent signal may be IMPA1 reads landing on the wrong feature — and any correlation it shows would then be inherited from the parent locus. The transcript is low enough that ambient RNA is also a live explanation. With no established function there is no mechanism against which a correlation could be judged.

## References

No primary literature I can cite with confidence.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.82× (z +9.1, q 7e-17, up in 20 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Radotinib (drug)]] 5 µM: 0.655× (z -3.8, q 0.099, down in 14 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Sacubitril_Valsartan (drug)]] 0.05 µM in 1 line (LoVo 0.0824×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALDH8A1]] (+0.88, fdr 7e-06), [[FNDC7]] (+0.87, fdr 7e-06), [[TRIM72]] (+0.83, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LMO7DN]] → it (grade B ⚠); 23 go from it, the strongest it → [[LINC01191]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14771.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.82×** | +9.1 | 7e-17 | 20/32 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.79×** | +9.0 | 8e-17 | 23/32 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.30×** | +8.7 | 7e-16 | 21/28 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.26×** | +8.6 | 8e-16 | 21/31 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.03×** | +8.3 | 1e-14 | 1/3 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.33×** | +6.9 | 5e-10 | 6/8 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.54×** | +5.6 | 2e-06 | 12/20 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.43×** | +5.5 | 3e-06 | 13/29 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.36×** | +5.3 | 7e-06 | 16/35 (LoVo, SW480, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.35×** | +5.3 | 7e-06 | 19/41 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.82×** | +5.2 | 1e-05 | 21/39 (A498, SW480, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **2.00×** | +4.3 | 9e-04 | 14/41 (LoVo, RKO, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.88×** | +3.9 | 0.004 | 9/39 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.93×** | +3.8 | 0.004 | 9/37 (A498, SW480, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +3.8 | 0.004 | 13/40 (A498, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.71×** | +3.3 | 0.028 | 12/39 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14771.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Sacubitril_Valsartan (drug)]] 0.05 µM in 1 line (LoVo 0.0824×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **0.655×** | -3.8 | 0.099 | 14/38 (RKO, C32, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.678× | -3.4 | 0.11 | 13/41 (RKO, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.558× | -3.4 | 0.11 | 11/34 (SK-MEL-2, C32, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.395× | -3.0 | 0.34 | 8/26 (SW480, RKO, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14771. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 6.82 | 0 | 1 | — | [[Sacubitril_Valsartan (drug)]] 0.05 µM 0.0824× (z -8.7) |
| [[A-172 (line)]] | wt | 0.378 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.588 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.724 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14771), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH8A1]] | +0.88 | +0.89 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[FNDC7]] | +0.87 | +0.87 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[TRIM72]] | +0.83 | +0.87 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[USP50]] | +0.83 | +0.83 / +0.79 | both halves | 7e-06 |  |
| [[XG]] | +0.81 | +0.73 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[MYOCOS]] | +0.81 | +0.79 / +0.75 | both halves | 7e-06 |  |
| [[OIT3]] | +0.80 | +0.78 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[PILRA]] | +0.80 | +0.79 / +0.77 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.80 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[DPYS]] | +0.80 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.80 | +0.79 / +0.81 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.80 | +0.82 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMO7DN]] | B | LMO7DN activity raises IMPA1P1's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 1.71× lower at baseline in the lines without LMO7DN | 0.005 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[LINC01291]] | B | LINC01291 activity raises IMPA1P1's level | lines that do not express LINC01291 (10) vs lines expressing it (40) | 1.61× lower at baseline in the lines without LINC01291 | 0.016 | ⚠ within organs, on part of the lines; also absent: ANTXR2, ENSG00000230479, PROCR; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers IMPA1P1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC2A9]] | B | SLC2A9 activity raises IMPA1P1's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 1.99× lower at baseline in the lines without SLC2A9 | 0.041 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[PLSCR2]] | B | PLSCR2 activity raises IMPA1P1's level | lines that do not express PLSCR2 (6) vs lines expressing it (44) | 1.65× lower at baseline in the lines without PLSCR2 | 0.079 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent |
| [[FAM3B]] | B | FAM3B activity raises IMPA1P1's level | lines that do not express FAM3B (12) vs lines expressing it (38) | 1.26× lower at baseline in the lines without FAM3B | 0.087 | ⚠ within organs, on part of the lines; also absent: TXNIP, CADPS2, PLAC4; maybe low, not absent |
| [[TRIM72]] | C | TRIM72 activity raises IMPA1P1's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 1.92× lower at baseline in the lines without TRIM72 | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 23, C 0. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01191]] | B | IMPA1P1 activity raises LINC01191's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 2.36× lower at baseline in the lines without IMPA1P1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[LINC01619]] | B | IMPA1P1 activity raises LINC01619's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 2.53× lower at baseline in the lines without IMPA1P1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[IDI2-AS1]] | B | IMPA1P1 activity raises IDI2-AS1's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.93× lower at baseline in the lines without IMPA1P1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[CCDC181]] | B | IMPA1P1 activity raises CCDC181's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.86× lower at baseline in the lines without IMPA1P1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[IRAG1-AS1]] | B | IMPA1P1 activity raises IRAG1-AS1's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.81× lower at baseline in the lines without IMPA1P1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | B | IMPA1P1 activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express IMPA1P1 (6) vs lines expressing it (42) | the lines without IMPA1P1: 0.83× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[ACOT12]] | B | IMPA1P1 activity raises ACOT12's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.78× lower at baseline in the lines without IMPA1P1 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[TMEM236]] | B | IMPA1P1 activity raises TMEM236's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 2.01× lower at baseline in the lines without IMPA1P1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[SELPLG]] | B | IMPA1P1 activity raises SELPLG's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.81× lower at baseline in the lines without IMPA1P1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[ANKDD1B]] | B | IMPA1P1 activity raises ANKDD1B's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.73× lower at baseline in the lines without IMPA1P1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[LINC02631]] | B | IMPA1P1 activity raises LINC02631's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without IMPA1P1 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[FAM151B]] | B | IMPA1P1 activity raises FAM151B's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.72× lower at baseline in the lines without IMPA1P1 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.869). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.9, -15.3); signed map (16.8, 10.1). **Vector** length 73.7, 12.7% of its response variance represented; |z| ≥ 3 in 1,247 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +8.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.0 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +9.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +3.8 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -3.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.8 | -3.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.8 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -0.5 |
|  | [[Bexarotene (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | inositol monophosphatase 1 pseudogene 1 |
| Locus type | pseudogene |
| Location | 8q21.13 — chr8:81,605,569-81,626,949 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously IMPA1P |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:33956](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33956) · Entrez [650747](https://www.ncbi.nlm.nih.gov/gene/650747) · Ensembl [ENSG00000251521](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000251521)

## Data

Gene col 14771: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14771); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14771, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14771]; `tensor/DDL_lfc|DDL_z.npy` [14771]; `embed/gene_vectors.npy` [14771]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14771 or target_col == 14771). Every well: [[IMPA1P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/IMPA1P1.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
