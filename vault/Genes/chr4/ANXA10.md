---
symbol: "ANXA10"
type: "gene"
col: 3057
ensembl_id: "ENSG00000109511"
name: "annexin A10"
location: "4q32.3"
module: 81
arm: "+"
pooled_cpm: 6.97
n_lines_expressing: 14
n_dd_up: 15
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 12
direction_downstream: 32
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# ANXA10

*annexin A10* — 4q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.47× (z +11.9, q 9e-30, up in 1 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.30× (z +8.5, q 2e-15, up in 4 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 0.526× (z -4.7, q 0.002, down in 8 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NTNG2]] (+0.68, fdr 1e-05), [[PTHLH]] (+0.67, fdr 7e-06), [[IL1B]] (+0.64, fdr 7e-06); moves opposite to [[FLVCR2]] (-0.64, fdr 7e-06), [[MT1E]] (-0.58, fdr 1e-05), [[CCBE1]] (-0.56, fdr 4e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 32 go from it, the strongest it → [[DENND3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3057.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.47×** | +11.9 | 9e-30 | 1/6 (KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.68×** | +11.2 | 9e-27 | 4/7 (SNU-423, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.58×** | +8.6 | 2e-15 | 3/6 (HT-29, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +8.5 | 2e-15 | 4/12 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +4.5 | 8e-04 | 4/12 (CFPAC-1, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +4.2 | 0.002 | 0/10 | top dose only | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.78×** | +4.2 | 0.002 | 2/12 (CFPAC-1, A549) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +3.9 | 0.007 | 2/9 (CFPAC-1, KATO III) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.66×** | +3.7 | 0.016 | 6/12 (HT-29, KATO III, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +3.6 | 0.017 | 2/12 (CFPAC-1, NCI-H1573) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.62×** | +3.5 | 0.023 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.61×** | +3.5 | 0.025 | 3/12 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.2 | 0.067 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.60×** | +3.1 | 0.070 | 1/8 (NCI-H460) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.56×** | +3.1 | 0.071 | 4/12 (NCI-H1573, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3057.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.526×** | -4.7 | 0.002 | 8/12 (NCI-H1792, HOP62, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.851× | -4.2 | 0.007 | 2/12 (NCI-H1792, HOP62) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.681×** | -4.0 | 0.013 | 9/12 (HOP62, SNU-423, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.586×** | -3.9 | 0.013 | 10/12 (NCI-H1792, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.593×** | -3.8 | 0.015 | 4/12 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.617×** | -3.5 | 0.040 | 8/12 (NCI-H1792, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.635×** | -3.3 | 0.064 | 9/12 (NCI-H1792, HOP62, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.637×** | -3.3 | 0.064 | 8/12 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **0.638×** | -3.3 | 0.064 | 6/12 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.657× | -3.1 | 0.12 | 7/12 (NCI-H1792, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3057. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 126 | 0 | 19 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0818× (z -15.2) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0370× (z -14.2) |
| [[HOP62 (line)]] | alt | 15.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -11.4) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Budesonide (drug)]] 0.5 µM 0.108× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 80.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -16.2) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0921× (z -13.4) |
| [[HT-29 (line)]] | alt | 18.6 | 3 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 14.3× (z +12.6) | [[Belinostat (drug)]] 5 µM 0.164× (z -8.6) |
| [[KATO III (line)]] | alt | 13.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0478× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 2.29 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.0685× (z -9.4) |
| [[A-172 (line)]] | wt | 0.854 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.486 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.966 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.808 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.680 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.874 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.998 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.780 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.647 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.707 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.995 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.856 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.735 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.947 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.700 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.700 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.680 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.901 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.613 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.852 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.636 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.879 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.592 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3057), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NTNG2]] | +0.68 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[PTHLH]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[IL1B]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[AADAC]] | +0.62 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[GCKR]] | +0.62 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[NGRN]] | +0.59 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[GJA1]] | +0.59 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[C6orf141]] | +0.58 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[IL33]] | +0.58 | +0.44 / +0.66 | both halves | 3e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[MANCR]] | +0.57 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[ANTXR2]] | +0.57 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[RDH10]] | +0.56 | +0.47 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLVCR2]] | -0.64 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[MT1E]] | -0.58 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[CCBE1]] | -0.56 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[ACSL1]] | -0.56 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[MAOA]] | -0.54 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[PDLIM1]] | -0.54 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[KLF9]] | -0.54 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[COPS8]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[TSC22D3]] | -0.53 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[CCND3]] | -0.52 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[SORT1]] | -0.51 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[MT1M]] | -0.51 | -0.44 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 4, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANXA10's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises ANXA10's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RTN4RL1]] | B | RTN4RL1 activity lowers ANXA10's level | lines that do not express RTN4RL1 (14) vs lines expressing it (36) | 2.24× higher at baseline in the lines without RTN4RL1 | 0.081 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |
| [[WNT7B]] | B | WNT7B activity raises ANXA10's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 1.94× lower at baseline in the lines without WNT7B | 0.098 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[PTGS2]] | C | PTGS2 activity raises ANXA10's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.30× lower at baseline in the lines without PTGS2 | 0.012 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4; co-absent with the target |
| [[ADAMTS9-AS2]] | C | ADAMTS9-AS2 activity raises ANXA10's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 1.92× lower at baseline in the lines without ADAMTS9-AS2 | 0.052 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2; co-absent with the target |
| [[LINC01705]] | C | LINC01705 activity raises ANXA10's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 1.74× lower at baseline in the lines without LINC01705 | 0.054 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises ANXA10's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 2.01× lower at baseline in the lines without LINC01411 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[GCKR]] | C | GCKR activity raises ANXA10's level | lines that do not express GCKR (24) vs lines expressing it (26) | 2.08× lower at baseline in the lines without GCKR | 0.057 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent; co-absent with the target |
| [[FOXC2]] | C | FOXC2 activity raises ANXA10's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 2.06× lower at baseline in the lines without FOXC2 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT; co-absent with the target |
| [[AADACP1]] | C | AADACP1 activity raises ANXA10's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 2.19× lower at baseline in the lines without AADACP1 | 0.095 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1; co-absent with the target |
| [[LYPLAL1-DT]] | C | LYPLAL1-DT activity raises ANXA10's level | lines that do not express LYPLAL1-DT (32) vs lines expressing it (18) | 2.27× lower at baseline in the lines without LYPLAL1-DT | 0.099 | ⚠ within organs, on part of the lines; also absent: EBF1, ANXA10, IRF4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 14, C 18. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DENND3]] | B | ANXA10 activity raises DENND3's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 1.93× lower at baseline in the lines without ANXA10 | 0.014 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP |
| [[TSC22D3]] | B | ANXA10 activity raises TSC22D3's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 2.29× lower at baseline in the lines without ANXA10 | 0.018 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP |
| [[LINC00536]] | B | ANXA10 activity raises LINC00536's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 2.25× lower at baseline in the lines without ANXA10 | 0.018 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP |
| [[VEGFC]] | B | ANXA10 activity raises VEGFC's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 3.18× lower at baseline in the lines without ANXA10 | 0.028 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP |
| [[SYNJ2]] | B | ANXA10 activity strengthens SYNJ2's drug response | lines that do not express ANXA10 (33) vs lines expressing it (12) | the lines without ANXA10 respond 0.53× as strongly (z diff +2.66); strongest at Panobinostat 5 µM: 0.70x vs 0.44x (z diff +4.1) | 0.039 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP; target measured in part of the lines; the reference differs; artifact flags |
| [[LIF]] | B | ANXA10 activity raises LIF's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 2.23× lower at baseline in the lines without ANXA10 | 0.044 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP |
| [[NHS]] | B | ANXA10 activity raises NHS's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 3.43× lower at baseline in the lines without ANXA10 | 0.045 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP |
| [[SPOCD1]] | B | ANXA10 activity raises SPOCD1's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 2.38× lower at baseline in the lines without ANXA10 | 0.051 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP |
| [[FZD8]] | B | ANXA10 activity raises FZD8's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 1.68× lower at baseline in the lines without ANXA10 | 0.061 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP |
| [[RABGEF1P3]] | B | ANXA10 activity raises RABGEF1P3's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 1.32× lower at baseline in the lines without ANXA10 | 0.062 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP |
| [[SYNJ2]] | B | ANXA10 activity raises SYNJ2's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 1.65× lower at baseline in the lines without ANXA10 | 0.070 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP |
| [[GPR68]] | B | ANXA10 activity raises GPR68's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 1.55× lower at baseline in the lines without ANXA10 | 0.079 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.630). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.8, 12.5); signed map (18.0, 50.5). **Vector** length 45.9, 14.2% of its response variance represented; |z| ≥ 3 in 362 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.1 | +1.5 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -2.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.1 | -1.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | annexin A10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.3 — chr4:168,092,537-168,187,736 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ANX14 |
| Gene groups (HGNC) | Annexins |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

UniProt [Q9UJ72](https://www.uniprot.org/uniprotkb/Q9UJ72) carries no function annotation.

**Summary**, from NCBI Gene [11199](https://www.ncbi.nlm.nih.gov/gene/11199):

> This gene encodes a member of the annexin family. Members of this calcium-dependent phospholipid-binding protein family play a role in the regulation of cellular growth and in signal transduction pathways. The function of this gene has not yet been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:534](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:534) · Entrez [11199](https://www.ncbi.nlm.nih.gov/gene/11199) · UniProt [Q9UJ72](https://www.uniprot.org/uniprotkb/Q9UJ72) · Ensembl [ENSG00000109511](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109511)

## Data

Gene col 3057: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3057); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3057, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3057]; `tensor/DDL_lfc|DDL_z.npy` [3057]; `embed/gene_vectors.npy` [3057]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3057 or target_col == 3057). Every well: [[ANXA10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANXA10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
