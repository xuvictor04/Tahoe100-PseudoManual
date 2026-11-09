---
symbol: "PDGFRA"
type: "gene"
col: 5614
ensembl_id: "ENSG00000134853"
name: "platelet derived growth factor receptor alpha"
location: "4q12"
module: 104
arm: "+"
pooled_cpm: 4.4
n_lines_expressing: 21
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 21
direction_downstream: 23
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# PDGFRA

*platelet derived growth factor receptor alpha* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.42× (z +13.3, q 1e-37, up in 2 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.75× (z +11.7, q 3e-29, up in 3 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.594× (z -4.3, q 0.011, down in 6 of 17 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 9 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (HOP62 0.0254×, SNU-1 0.109×, NCI-H1792 0.0757×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.0767×; ⚠ toxic); [[Digitoxin (drug)]] 0.5 µM in 1 line (SNU-1 0.0908×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3RF3]] (+0.70, fdr 8e-06), [[DAAM2]] (+0.57, fdr 1e-05), [[ITGA8]] (+0.57, fdr 1e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[DCN]] → it (grade C ⚠); 23 go from it, the strongest it → [[HMGA2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5614.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.42×** | +13.3 | 1e-37 | 2/6 (HS-578T, hTERT-HPNE) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.05×** | +13.2 | 1e-37 | 2/8 (CFPAC-1, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.75×** | +11.7 | 3e-29 | 3/11 (A-172, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.32×** | +11.1 | 2e-26 | 3/6 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.08×** | +8.5 | 3e-15 | 11/17 (A549, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +7.6 | 3e-12 | 4/12 (A-172, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.92×** | +5.3 | 7e-06 | 8/16 (RPMI-7951, hTERT-HPNE, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +4.6 | 3e-04 | 6/14 (LOX-IMVI, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.61×** | +3.9 | 0.006 | 6/17 (RPMI-7951, hTERT-HPNE, …) | all doses, flat |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.92×** | +3.8 | 0.008 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.37×** | +3.7 | 0.012 | 2/5 (HS-578T, HOP62) | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.34×** | +3.6 | 0.013 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.55×** | +3.6 | 0.013 | 4/16 (RPMI-7951, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.55×** | +3.6 | 0.013 | 7/15 (RPMI-7951, hTERT-HPNE, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.55×** | +3.6 | 0.014 | 5/14 (RPMI-7951, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.50×** | +3.3 | 0.032 | 6/16 (hTERT-HPNE, RPMI-7951, …) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.048 | 0/13 | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.71×** | +3.1 | 0.053 | 1/11 (HS-578T) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +3.0 | 0.076 | 4/15 (A-172, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5614.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 9 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (HOP62 0.0254×, SNU-1 0.109×, NCI-H1792 0.0757×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.0767×; ⚠ toxic); [[Digitoxin (drug)]] 0.5 µM in 1 line (SNU-1 0.0908×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.594×** | -4.3 | 0.011 | 6/17 (SNU-1, RPMI-7951, …) | two highest doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.663× | -3.4 | 0.21 | 9/17 (SNU-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.682× | -3.1 | 0.26 | 7/17 (RPMI-7951, SNU-1, …) | rises with dose | position effect removed |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.676× | -3.0 | 0.26 | 2/17 (LOX-IMVI, C-33 A) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5614. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 99.4 | 0 | 8 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0767× (z -13.5) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0908× (z -13.1) |
| [[HOP62 (line)]] | alt | 13.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0254× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 1.30 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.8× (z +10.2) | — |
| [[C32 (line)]] | wt | 4.81 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0333× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 2.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0757× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A-427 (line)]] | wt | 0.539 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.555 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.872 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.767 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.454 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.450 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.507 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.500 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.794 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.863 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.610 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.453 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5614), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3RF3]] | +0.70 | +0.58 / +0.74 | both halves | 8e-06 | **novel candidate** |
| [[DAAM2]] | +0.57 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[ITGA8]] | +0.57 | +0.49 / +0.56 | both halves | 1e-05 | STRING 443 |
| [[DCN]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 | STRING 826 |
| [[COL4A1]] | +0.57 | +0.48 / +0.53 | both halves | 2e-05 | pathway: Signaling by PDGF; STRING 440 |
| [[ATOH8]] | +0.55 | +0.40 / +0.62 | both halves | 4e-05 |  |
| [[COL6A3]] | +0.55 | +0.55 / +0.45 | both halves | 3e-05 | pathway: Signaling by PDGF; STRING 556 |
| [[WNT5A]] | +0.54 | +0.47 / +0.56 | both halves | 2e-05 | STRING 515 |
| [[DNER]] | +0.54 | +0.38 / +0.60 | both halves | 6e-05 |  |
| [[RIPOR2]] | +0.54 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[COL4A2]] | +0.54 | +0.58 / +0.45 | both halves | 3e-05 | pathway: Signaling by PDGF |
| [[HSD11B1]] | +0.53 | +0.45 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 0, C 21. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCN]] | C | DCN activity raises PDGFRA's level | lines that do not express DCN (39) vs lines expressing it (11) | 4.53× lower at baseline in the lines without DCN | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, CARMN, THY1; co-absent with the target |
| [[GYPC]] | C | GYPC activity raises PDGFRA's level | lines that do not express GYPC (35) vs lines expressing it (15) | 3.00× lower at baseline in the lines without GYPC | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4; co-absent with the target |
| [[CARMN]] | C | CARMN activity raises PDGFRA's level | lines that do not express CARMN (40) vs lines expressing it (10) | 4.01× lower at baseline in the lines without CARMN | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN; co-absent with the target |
| [[PRRX1]] | C | PRRX1 activity raises PDGFRA's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 2.87× lower at baseline in the lines without PRRX1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[HTRA3]] | C | HTRA3 activity raises PDGFRA's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 2.68× lower at baseline in the lines without HTRA3 | 0.017 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN; co-absent with the target |
| [[RNF175]] | C | RNF175 activity raises PDGFRA's level | lines that do not express RNF175 (30) vs lines expressing it (20) | 2.72× lower at baseline in the lines without RNF175 | 0.022 | ⚠ within organs, on part of the lines; also absent: SCG2, ENSG00000266450, MIR493HG; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises PDGFRA's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.51× lower at baseline in the lines without PDGFRB | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises PDGFRA's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 2.79× lower at baseline in the lines without APCDD1L | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[LINC01098]] | C | LINC01098 activity raises PDGFRA's level | lines that do not express LINC01098 (36) vs lines expressing it (14) | 3.10× lower at baseline in the lines without LINC01098 | 0.035 | ⚠ within organs, on part of the lines; also absent: LINC02109, GREM1, ENSG00000288098; maybe low, not absent; co-absent with the target |
| [[FOXC2]] | C | FOXC2 activity raises PDGFRA's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 2.22× lower at baseline in the lines without FOXC2 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT; co-absent with the target |
| [[TWIST1]] | C | TWIST1 activity raises PDGFRA's level | lines that do not express TWIST1 (26) vs lines expressing it (24) | 2.32× lower at baseline in the lines without TWIST1 | 0.038 | ⚠ within organs, on part of the lines; also absent: PCDH10, MDGA2, FAP; co-absent with the target |
| [[LOX]] | C | LOX activity raises PDGFRA's level | lines that do not express LOX (31) vs lines expressing it (19) | 2.28× lower at baseline in the lines without LOX | 0.047 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 7, C 16. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGA2-AS1]] | B | PDGFRA activity raises HMGA2-AS1's level | lines that do not express PDGFRA (29) vs lines expressing it (21) | 1.42× lower at baseline in the lines without PDGFRA | 0.042 | ⚠ within organs, on part of the lines; also absent: LRCH2, MAGI2-AS3, THY1 |
| [[AKAP12]] | B | PDGFRA activity raises AKAP12's level | lines that do not express PDGFRA (29) vs lines expressing it (21) | 2.75× lower at baseline in the lines without PDGFRA | 0.056 | ⚠ within organs, on part of the lines; also absent: LRCH2, MAGI2-AS3, THY1 |
| [[ITGA5]] | B | PDGFRA activity raises ITGA5's level | lines that do not express PDGFRA (29) vs lines expressing it (21) | 2.51× lower at baseline in the lines without PDGFRA | 0.062 | ⚠ within organs, on part of the lines; also absent: LRCH2, MAGI2-AS3, THY1 |
| [[HES1]] | B | PDGFRA activity raises HES1's level | compounds that target PDGFRA: 2 of 3 lower it (Ponatinib, c-Kit-IN-1) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[PKD1]] | B | PDGFRA activity lowers PKD1's level | compounds that target PDGFRA: 2 of 3 raise it (Ponatinib, c-Kit-IN-1) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[SAA2]] | B | PDGFRA activity raises SAA2's level | compounds that target PDGFRA: 2 of 3 lower it (Ponatinib, c-Kit-IN-1) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[HMGA2]] | B | PDGFRA activity raises HMGA2's level | lines that do not express PDGFRA (29) vs lines expressing it (21) | 2.02× lower at baseline in the lines without PDGFRA | 0.097 | ⚠ within organs, on part of the lines; also absent: LRCH2, MAGI2-AS3, THY1 |
| [[LOX]] | C | PDGFRA activity raises LOX's level | lines that do not express PDGFRA (29) vs lines expressing it (21) | 4.99× lower at baseline in the lines without PDGFRA | 0.011 | ⚠ within organs, on part of the lines; also absent: LRCH2, MAGI2-AS3, THY1; co-absent with the target |
| [[LINC01098]] | C | PDGFRA activity raises LINC01098's level | lines that do not express PDGFRA (29) vs lines expressing it (21) | 3.40× lower at baseline in the lines without PDGFRA | 0.015 | ⚠ within organs, on part of the lines; also absent: LRCH2, MAGI2-AS3, THY1; co-absent with the target |
| [[PDGFRB]] | C | PDGFRA activity raises PDGFRB's level | lines that do not express PDGFRA (29) vs lines expressing it (21) | 4.57× lower at baseline in the lines without PDGFRA | 0.020 | ⚠ within organs, on part of the lines; also absent: LRCH2, MAGI2-AS3, THY1; co-absent with the target |
| [[PRRX1]] | C | PDGFRA activity raises PRRX1's level | lines that do not express PDGFRA (29) vs lines expressing it (21) | 5.47× lower at baseline in the lines without PDGFRA | 0.021 | ⚠ within organs, on part of the lines; also absent: LRCH2, MAGI2-AS3, THY1; co-absent with the target |
| [[PAPPA]] | C | PDGFRA activity raises PAPPA's level | lines that do not express PDGFRA (29) vs lines expressing it (21) | 3.47× lower at baseline in the lines without PDGFRA | 0.023 | ⚠ within organs, on part of the lines; also absent: LRCH2, MAGI2-AS3, THY1; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.671). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (53.3, 23.6); signed map (24.8, 39.5). **Vector** length 46.0, 11.4% of its response variance represented; |z| ≥ 3 in 505 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +8.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.1 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.3 | +3.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.3 | +5.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.2 | +2.5 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -0.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | platelet derived growth factor receptor alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:54,229,280-54,298,245 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD140a, PDGFR2, GAS9 |
| Gene groups (HGNC) | CD molecules; I-set domain containing; Platelet derived growth factor receptor family |
| Reactome | 16 pathways, smallest: Signaling by PDGFRA extracellular domain mutants; Signaling by PDGFRA transmembrane, juxtamembrane and kinase domain mutants; Signaling by PDGFR in disease |
| Matched by | ensembl_id |

**Function**, from UniProt [P16234](https://www.uniprot.org/uniprotkb/P16234) (Platelet-derived growth factor receptor alpha):

> Tyrosine-protein kinase that acts as a cell-surface receptor for PDGFA, PDGFB and PDGFC and plays an essential role in the regulation of embryonic development, cell proliferation, survival and chemotaxis. Depending on the context, promotes or inhibits cell proliferation and cell migration. Plays an important role in the differentiation of bone marrow-derived mesenchymal stem cells. Required for normal skeleton development and cephalic closure during embryonic development. Required for normal …

**Summary**, from NCBI Gene [5156](https://www.ncbi.nlm.nih.gov/gene/5156):

> This gene encodes a cell surface tyrosine kinase receptor for members of the platelet-derived growth factor family. These growth factors are mitogens for cells of mesenchymal origin. The identity of the growth factor bound to a receptor monomer determines whether the functional receptor is a homodimer or a heterodimer, composed of both platelet-derived growth factor receptor alpha and beta polypeptides. Studies suggest that this gene plays a role in organ development, wound healing, and tumor …

**Accessions** — [HGNC:8803](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8803) · Entrez [5156](https://www.ncbi.nlm.nih.gov/gene/5156) · UniProt [P16234](https://www.uniprot.org/uniprotkb/P16234) · Ensembl [ENSG00000134853](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134853)

## Data

Gene col 5614: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5614); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5614, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5614]; `tensor/DDL_lfc|DDL_z.npy` [5614]; `embed/gene_vectors.npy` [5614]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5614 or target_col == 5614). Every well: [[PDGFRA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDGFRA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
