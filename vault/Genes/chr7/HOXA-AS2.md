---
symbol: "HOXA-AS2"
type: "gene"
col: 14813
ensembl_id: "ENSG00000253552"
name: "HOXA cluster antisense RNA 2"
location: "7p15.2"
module: 23
arm: "+"
pooled_cpm: 4.68
n_lines_expressing: 47
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 8
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# HOXA-AS2

*HOXA cluster antisense RNA 2* — 7p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.87× (z +18.1, q 0e+00, up in 33 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.490× (z -6.8, q 5e-09, down in 22 of 43 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM: 0.747× (z -4.0, q 0.010, down in 8 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (NCI-H1792 0.0446×, HEC-1-A 0.164×; ⚠ cell-cycle shift, explains ~38% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (HEC-1-A 0.167×, Panc 03.27 0.136×; ⚠ cell-cycle shift, explains ~42% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (Panc 03.27 0.135×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXB-AS3]] (+0.72, fdr 1e-05), [[PPP1R42]] (+0.70, fdr 1e-05), [[HCG27]] (+0.70, fdr 1e-05); moves opposite to [[RRP1B]] (-0.61, fdr 3e-05), [[MLX]] (-0.59, fdr 1e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HOXA3]] → it (grade B ⚠); 8 go from it, the strongest it → [[CMAHP]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14813.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.87×** | +18.1 | 0e+00 | 33/35 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +8.4 | 1e-14 | 3/9 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.26×** | +6.7 | 3e-09 | 6/13 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +6.6 | 8e-09 | 12/23 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +5.3 | 1e-05 | 13/34 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +5.1 | 3e-05 | 15/33 (SW48, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.9 | 7e-05 | 12/31 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.003 | 10/41 (PANC-1, HOP62, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.0 | 0.005 | 9/36 (RPMI-7951, PANC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.005 | 9/43 (PANC-1, HepG2/C3A, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +3.8 | 0.008 | 7/23 (CFPAC-1, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.013 | 6/41 (HT-29, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.017 | 10/42 (NCI-H1792, HOP62, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.44×** | +3.5 | 0.022 | 6/41 (HEC-1-A, NCI-H1792, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.029 | 10/41 (AsPC-1, A-172, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.60×** | +3.2 | 0.057 | 4/35 (HEC-1-A, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.37×** | +3.0 | 0.092 | 5/42 (A549, CFPAC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14813.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (NCI-H1792 0.0446×, HEC-1-A 0.164×; ⚠ cell-cycle shift, explains ~38% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (HEC-1-A 0.167×, Panc 03.27 0.136×; ⚠ cell-cycle shift, explains ~42% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (Panc 03.27 0.135×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.490×** | -6.8 | 5e-09 | 22/43 (NCI-H1792, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.573×** | -5.3 | 3e-05 | 21/42 (HEC-1-A, Panc 03.27, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.586×** | -5.1 | 6e-05 | 18/42 (Panc 03.27, HEC-1-A, …) | rises with dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **0.747×** | -4.0 | 0.010 | 8/41 (Hs 766T, C32, …) | top dose only |  |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | **0.772×** | -3.5 | 0.051 | 6/43 (MIA PaCa-2, J82, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.709×** | -3.3 | 0.087 | 11/40 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.715× | -3.1 | 0.15 | 10/42 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.729× | -3.0 | 0.17 | 8/43 (COLO 205, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.47 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14813. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 12.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 19.0 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.164× (z -10.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H1792 (line)]] | alt | 14.5 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0446× (z -12.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-172 (line)]] | wt | 1.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +8.7) | — |
| [[A498 (line)]] | wt | 11.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 2.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.89× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 3.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +10.4) | — |
| [[SW1417 (line)]] | alt | 4.32 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0807× (z -8.9) ⚠ transcription drop |
| [[SW480 (line)]] | alt | 2.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +8.5) | — |
| [[A-427 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.946 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.43 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14813), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXB-AS3]] | +0.72 | +0.50 / +0.72 | both halves | 1e-05 | same gene group |
| [[PPP1R42]] | +0.70 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[HCG27]] | +0.70 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[CHMP3-AS1]] | +0.68 | +0.48 / +0.71 | both halves | 2e-05 | same gene group |
| [[ANKHD1-DT]] | +0.68 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[MED28-DT]] | +0.68 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[CTDSPL2-DT]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[CEACAM16-AS1]] | +0.67 | +0.61 / +0.52 | both halves | 1e-05 | same gene group |
| [[SLC23A1]] | +0.67 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[C2CD5-AS1]] | +0.67 | +0.52 / +0.60 | both halves | 1e-05 | same gene group |
| [[KLRK1-AS1]] | +0.67 | +0.46 / +0.58 | both halves | 2e-05 | same gene group |
| [[PAXBP1-AS1]] | +0.66 | +0.52 / +0.58 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP1B]] | -0.61 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[MLX]] | -0.59 | -0.53 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA3]] | B | HOXA3 activity raises HOXA-AS2's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 2.11× lower at baseline in the lines without HOXA3 | 0.005 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers HOXA-AS2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[VAMP8]] | B | VAMP8 activity raises HOXA-AS2's level | lines that do not express VAMP8 (14) vs lines expressing it (36) | 1.81× lower at baseline in the lines without VAMP8 | 0.067 | ⚠ within organs, on part of the lines; also absent: CDCP1, CHMP4C, EVPL; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises HOXA-AS2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PTGIS]] | B | PTGIS activity raises HOXA-AS2's level | lines that do not express PTGIS (39) vs lines expressing it (11) | 1.71× lower at baseline in the lines without PTGIS | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, PREX2, GCG |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CMAHP]] | C | HOXA-AS2 activity lowers CMAHP's level | lines that do not express HOXA-AS2 (3) vs lines expressing it (47) | 2.40× higher at baseline in the lines without HOXA-AS2 | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: HFE, COTL1, ACCS; maybe low, not absent |
| [[SCYL3]] | C | HOXA-AS2 activity lowers SCYL3's level | lines that do not express HOXA-AS2 (3) vs lines expressing it (47) | 1.75× higher at baseline in the lines without HOXA-AS2 | 0.028 | ⚠ few lines (3 vs 47); across organs; also absent: HFE, COTL1, ACCS; maybe low, not absent |
| cells under [[Vemurafenib (drug)]] 5 µM | C | HOXA-AS2 activity raises the cells' numbers under Vemurafenib 5 µM (protects the cells) | lines that do not express HOXA-AS2 (3) vs lines expressing it (45) | the lines without HOXA-AS2: 0.80× the cells of the other lines | 0.062 | ⚠ few lines (3 vs 47); across organs; also absent: HFE, COTL1, ACCS; maybe low, not absent |
| cells under [[PF-06260933 (drug)]] 5 µM | C | HOXA-AS2 activity lowers the cells' numbers under PF-06260933 5 µM (makes them more sensitive) | lines that do not express HOXA-AS2 (3) vs lines expressing it (45) | the lines without HOXA-AS2: 1.53× the cells of the other lines | 0.064 | ⚠ few lines (3 vs 47); across organs; also absent: HFE, COTL1, ACCS; maybe low, not absent |
| [[HOXA3]] | C | HOXA-AS2 activity raises HOXA3's level | lines that do not express HOXA-AS2 (3) vs lines expressing it (47) | 5.06× lower at baseline in the lines without HOXA-AS2 | 0.065 | ⚠ few lines (3 vs 47); across organs; also absent: HFE, COTL1, ACCS; maybe low, not absent |
| cells under [[IQ 1 (drug)]] 5 µM | C | HOXA-AS2 activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express HOXA-AS2 (3) vs lines expressing it (45) | the lines without HOXA-AS2: 0.73× the cells of the other lines | 0.075 | ⚠ few lines (3 vs 47); across organs; also absent: HFE, COTL1, ACCS; maybe low, not absent |
| [[FLJ40194]] | C | HOXA-AS2 activity lowers FLJ40194's level | lines that do not express HOXA-AS2 (3) vs lines expressing it (47) | 1.26× higher at baseline in the lines without HOXA-AS2 | 0.088 | ⚠ few lines (3 vs 47); across organs; also absent: HFE, COTL1, ACCS; maybe low, not absent |
| [[MALINC1]] | C | HOXA-AS2 activity raises MALINC1's level | lines that do not express HOXA-AS2 (3) vs lines expressing it (47) | 1.80× lower at baseline in the lines without HOXA-AS2 | 0.098 | ⚠ few lines (3 vs 47); across organs; also absent: HFE, COTL1, ACCS; maybe low, not absent |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.639). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (10.6, 23.4); signed map (31.2, -0.7). **Vector** length 68.7, 12.1% of its response variance represented; |z| ≥ 3 in 839 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.4 | +18.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +2.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.8 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.0 | -5.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.9 | -5.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.6 | -6.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | HOXA cluster antisense RNA 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7p15.2 — chr7:27,107,777-27,134,302 (+) |
| Ensembl biotype | lncRNA |
| Also known as | HOXA3as |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [285943](https://www.ncbi.nlm.nih.gov/gene/285943):

> This gene produces a long non-coding RNA that promotes cell proliferation. This transcript may interact with enhancer of zeste homolog 2 Polycomb repressive complex to repress gene expression. [provided by RefSeq, Dec 2017]

**Accessions** — [HGNC:43745](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43745) · Entrez [285943](https://www.ncbi.nlm.nih.gov/gene/285943) · Ensembl [ENSG00000253552](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253552)

## Data

Gene col 14813: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14813); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14813, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14813]; `tensor/DDL_lfc|DDL_z.npy` [14813]; `embed/gene_vectors.npy` [14813]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14813 or target_col == 14813). Every well: [[HOXA-AS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXA-AS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
