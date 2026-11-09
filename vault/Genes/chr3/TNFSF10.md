---
symbol: "TNFSF10"
type: "gene"
col: 4298
ensembl_id: "ENSG00000121858"
name: "TNF superfamily member 10"
location: "3q26.31"
module: 70
arm: "+"
pooled_cpm: 22.68
n_lines_expressing: 26
n_dd_up: 20
n_dd_down: 50
n_dd_up_clean: 19
n_dd_down_clean: 45
in_vector_space: true
direction_upstream: 58
direction_downstream: 69
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# TNFSF10

*TNF superfamily member 10* — 3q26.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 2.41× (z +6.4, q 7e-08, up in 20 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 50 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.296× (z -9.2, q 3e-17, down in 23 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPSTI1]] (+0.81, fdr 7e-06), [[MX2]] (+0.80, fdr 7e-06), [[CFB]] (+0.80, fdr 7e-06).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 58 arrows point to it, the strongest [[GBP2]] → it (grade B ⚠); 69 go from it, the strongest it → [[LGALS9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 1 with an alert ⚠; shown: the 15 strongest. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4298.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **2.41×** | +6.4 | 7e-08 | 20/23 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **2.14×** | +5.6 | 6e-06 | 17/23 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **2.00×** | +5.5 | 6e-06 | 20/24 (CFPAC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.79×** | +5.5 | 6e-06 | 20/24 (CFPAC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.81×** | +5.3 | 1e-05 | 19/24 (CFPAC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.57×** | +4.7 | 2e-04 | 20/24 (CFPAC-1, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.70×** | +4.1 | 0.004 | 18/24 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.12×** | +4.0 | 0.004 | 17/24 (CFPAC-1, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **2.04×** | +3.8 | 0.009 | 13/24 (CFPAC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.42×** | +3.8 | 0.009 | 17/24 (CFPAC-1, Hs 766T, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.64×** | +3.6 | 0.019 | 14/24 (CFPAC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | **1.59×** | +3.4 | 0.030 | 11/23 (BT-474, SW1417, …) | inconsistent across doses | position effect removed |
| [[Capmatinib (drug)]] 5 µM |  | **2.31×** | +3.3 | 0.037 | 9/22 (CFPAC-1, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.54×** | +3.3 | 0.037 | 11/23 (BT-474, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.53×** | +3.3 | 0.041 | 9/24 (A-172, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 50 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4298.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.296×** | -9.2 | 3e-17 | 23/23 (LoVo, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.465×** | -8.1 | 1e-13 | 21/23 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.347×** | -8.0 | 3e-13 | 21/24 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.353×** | -7.8 | 7e-13 | 20/24 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.400×** | -6.9 | 6e-10 | 21/24 (A498, NCI-H1792, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.419×** | -6.5 | 6e-09 | 17/24 (KATO III, A498, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.432×** | -6.3 | 2e-08 | 19/24 (A498, A-172, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.555×** | -6.3 | 3e-08 | 18/24 (KATO III, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.436×** | -6.2 | 3e-08 | 20/24 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.570×** | -6.0 | 1e-07 | 22/24 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.455×** | -5.9 | 2e-07 | 17/24 (AsPC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.459×** | -5.9 | 2e-07 | 19/23 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.459×** | -5.9 | 2e-07 | 20/24 (BT-474, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.462×** | -5.8 | 2e-07 | 19/24 (HT-29, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.467×** | -5.7 | 4e-07 | 18/24 (RPMI-7951, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.482×** | -5.2 | 7e-06 | 19/24 (BT-474, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.503×** | -5.2 | 8e-06 | 19/24 (HOP62, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4298. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 53.1 | 0 | 11 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0202× (z -16.2) |
| [[COLO 205 (line)]] | alt | 113 | 0 | 11 | — | [[Homoharringtonine (drug)]] 5 µM 0.0761× (z -15.6) |
| [[RPMI-7951 (line)]] | alt | 33.1 | 0 | 10 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.101× (z -12.2) |
| [[A498 (line)]] | wt | 45.0 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0608× (z -20.2) |
| [[SW480 (line)]] | alt | 14.9 | 0 | 8 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.122× (z -12.3) |
| [[KATO III (line)]] | alt | 36.9 | 0 | 6 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0947× (z -11.6) |
| [[HT-29 (line)]] | alt | 39.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -16.9) |
| [[LoVo (line)]] | wt | 12.3 | 0 | 5 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0177× (z -18.1) |
| [[A-172 (line)]] | wt | 18.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 237 | 0 | 4 | — | [[Auranofin (drug)]] 5 µM 0.121× (z -13.3) |
| [[CFPAC-1 (line)]] | alt | 61.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -9.2) |
| [[SNU-423 (line)]] | alt | 114 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -15.6) |
| [[MIA PaCa-2 (line)]] | alt | 9.42 | 1 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 2.53× (z +9.3) ⚠ position not correctable | [[Tofacitinib (drug)]] 5 µM 0.109× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 14.2 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.109× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 8.86 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0195× (z -11.9) |
| [[HOP62 (line)]] | alt | 22.4 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.158× (z -9.3) |
| [[Hs 766T (line)]] | wt | 22.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -11.2) |
| [[J82 (line)]] | alt | 8.50 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.2× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 47.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.198× (z -8.6) |
| [[SW1417 (line)]] | alt | 33.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.174× (z -9.1) |
| [[A-427 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.52 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.05 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.27 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.44 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.98 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4298), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPSTI1]] | +0.81 | +0.73 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[MX2]] | +0.80 | +0.74 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 452 |
| [[CFB]] | +0.80 | +0.75 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[GBP4]] | +0.80 | +0.70 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[RSAD2]] | +0.77 | +0.71 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 541 |
| [[XAF1]] | +0.77 | +0.67 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 582 |
| [[TRANK1]] | +0.77 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[TLR3]] | +0.76 | +0.69 / +0.82 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 537 |
| [[IFI44]] | +0.76 | +0.67 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 500 |
| [[APOL1]] | +0.76 | +0.69 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[TMEM140]] | +0.75 | +0.68 / +0.79 | both halves | 7e-06 |  |
| [[PSMB9]] | +0.75 | +0.69 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*58 arrows, 58 of them with an alert ⚠; grade A 0, B 34, C 24. Shown: the 12 strongest; 46 more arrows (46 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP2]] | B | GBP2 activity raises TNFSF10's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 4.34× lower at baseline in the lines without GBP2 | 0.005 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[GBP1]] | B | GBP1 activity raises TNFSF10's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 3.37× lower at baseline in the lines without GBP1 | 0.010 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[MX2]] | B | MX2 activity raises TNFSF10's level | lines that do not express MX2 (16) vs lines expressing it (34) | 3.17× lower at baseline in the lines without MX2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: NRP1, SLC15A3, DEPP1 |
| [[OASL]] | B | OASL activity raises TNFSF10's level | lines that do not express OASL (10) vs lines expressing it (40) | 3.33× lower at baseline in the lines without OASL | 0.020 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[LGALS9]] | B | LGALS9 activity raises TNFSF10's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 3.73× lower at baseline in the lines without LGALS9 | 0.024 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[CTSS]] | B | CTSS activity raises TNFSF10's level | lines that do not express CTSS (15) vs lines expressing it (35) | 2.88× lower at baseline in the lines without CTSS | 0.027 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises TNFSF10's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 3.30× lower at baseline in the lines without ELF3-AS1 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[XAF1]] | B | XAF1 activity raises TNFSF10's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 3.03× lower at baseline in the lines without XAF1 | 0.032 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[GBP4]] | B | GBP4 activity raises TNFSF10's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.60× lower at baseline in the lines without GBP4 | 0.035 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[IFIT2]] | B | IFIT2 activity raises TNFSF10's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 3.12× lower at baseline in the lines without IFIT2 | 0.035 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[IFI44L]] | B | IFI44L activity raises TNFSF10's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 2.39× lower at baseline in the lines without IFI44L | 0.040 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[RBM47]] | B | RBM47 activity raises TNFSF10's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 2.73× lower at baseline in the lines without RBM47 | 0.040 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |

### Downstream of this gene

*69 arrows, 69 of them with an alert ⚠; grade A 0, B 50, C 19. Shown: the 12 strongest; 57 more arrows (57 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGALS9]] | B | TNFSF10 activity raises LGALS9's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 2.83× lower at baseline in the lines without TNFSF10 | 0.004 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[GBP2]] | B | TNFSF10 activity raises GBP2's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 3.06× lower at baseline in the lines without TNFSF10 | 0.004 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[GBP1]] | B | TNFSF10 activity raises GBP1's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 3.27× lower at baseline in the lines without TNFSF10 | 0.006 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[STS]] | B | TNFSF10 activity raises STS's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 2.84× lower at baseline in the lines without TNFSF10 | 0.008 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[RBM47]] | B | TNFSF10 activity raises RBM47's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 3.17× lower at baseline in the lines without TNFSF10 | 0.008 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[RSAD2]] | B | TNFSF10 activity raises RSAD2's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 2.98× lower at baseline in the lines without TNFSF10 | 0.013 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[OAS2]] | B | TNFSF10 activity raises OAS2's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 2.85× lower at baseline in the lines without TNFSF10 | 0.014 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[OAS1]] | B | TNFSF10 activity raises OAS1's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 2.39× lower at baseline in the lines without TNFSF10 | 0.015 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[CTSS]] | B | TNFSF10 activity raises CTSS's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 2.67× lower at baseline in the lines without TNFSF10 | 0.016 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[TMEM62]] | B | TNFSF10 activity raises TMEM62's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 1.85× lower at baseline in the lines without TNFSF10 | 0.018 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[MX2]] | B | TNFSF10 activity raises MX2's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 3.31× lower at baseline in the lines without TNFSF10 | 0.022 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[PSMB10]] | B | TNFSF10 activity raises PSMB10's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 1.62× lower at baseline in the lines without TNFSF10 | 0.023 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.828). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.7, 51.1); signed map (61.6, 29.2). **Vector** length 123, 45.3% of its response variance represented; |z| ≥ 3 in 1,090 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.58 to 19); *Antigen processing-Cross presentation* (reactome, mean cos +0.59 to 14); *Interferon gamma signaling* (reactome, mean cos +0.59 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +5.0 | +6.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.5 | +5.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.4 | +5.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.9 | +5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.9 | +5.6 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -5.3 | -6.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.5 | -6.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.2 | -4.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.0 | -6.3 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.0 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | TNF superfamily member 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.31 — chr3:172,505,508-172,523,475 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRAIL, Apo-2L, TL2, CD253, TANCR |
| Gene groups (HGNC) | CD molecules; Tumor necrosis factor superfamily |
| Hallmark sets | INFLAMMATORY_RESPONSE, APOPTOSIS, IL2_STAT5_SIGNALING, INTERFERON_GAMMA_RESPONSE |
| Reactome | 12 pathways, smallest: TRAIL  signaling; CASP8 activity is inhibited; Dimerization of procaspase-8 |
| Matched by | ensembl_id |

**Function**, from UniProt [P50591](https://www.uniprot.org/uniprotkb/P50591) (Tumor necrosis factor ligand superfamily member 10):

> Cytokine that binds to TNFRSF10A/TRAILR1, TNFRSF10B/TRAILR2, TNFRSF10C/TRAILR3, TNFRSF10D/TRAILR4 and possibly also to TNFRSF11B/OPG. Induces apoptosis. Its activity may be modulated by binding to the decoy receptors TNFRSF10C/TRAILR3, TNFRSF10D/TRAILR4 and TNFRSF11B/OPG that cannot induce apoptosis.

**Summary**, from NCBI Gene [8743](https://www.ncbi.nlm.nih.gov/gene/8743):

> The protein encoded by this gene is a cytokine that belongs to the tumor necrosis factor (TNF) ligand family. This protein preferentially induces apoptosis in transformed and tumor cells, but does not appear to kill normal cells although it is expressed at a significant level in most normal tissues. This protein binds to several members of TNF receptor superfamily including TNFRSF10A/TRAILR1, TNFRSF10B/TRAILR2, TNFRSF10C/TRAILR3, TNFRSF10D/TRAILR4, and possibly also to TNFRSF11B/OPG. The …

**Accessions** — [HGNC:11925](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11925) · Entrez [8743](https://www.ncbi.nlm.nih.gov/gene/8743) · UniProt [P50591](https://www.uniprot.org/uniprotkb/P50591) · Ensembl [ENSG00000121858](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121858)

## Data

Gene col 4298: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4298); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4298, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4298]; `tensor/DDL_lfc|DDL_z.npy` [4298]; `embed/gene_vectors.npy` [4298]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4298 or target_col == 4298). Every well: [[TNFSF10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFSF10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
