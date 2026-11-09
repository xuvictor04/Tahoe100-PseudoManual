---
symbol: "KRT7"
type: "gene"
col: 5713
ensembl_id: "ENSG00000135480"
name: "keratin 7"
location: "12q13.13"
module: 98
arm: "+"
pooled_cpm: 102.97
n_lines_expressing: 16
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 10
direction_downstream: 18
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# KRT7

*keratin 7* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.60× (z +15.2, q 0e+00, up in 13 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 3.21× (z +9.9, q 7e-21, up in 12 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.509× (z -6.0, q 1e-06, down in 12 of 14 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGD4]] (+0.60, fdr 1e-05), [[KRT86]] (+0.59, fdr 1e-05, ⚠ same locus), [[AHNAK]] (+0.58, fdr 2e-05), [[DNAH5]] (+0.57, fdr 3e-05); moves opposite to [[RABEP2]] (-0.49, fdr 3e-05), [[LINC02210-CRHR1]] (-0.48, fdr 4e-05), [[ZNRF1]] (-0.46, fdr 1e-04).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[KRT86]] → it (grade B ⚠); 18 go from it, the strongest it → [[ABCC3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5713.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.60×** | +15.2 | 0e+00 | 13/15 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.83×** | +13.0 | 6e-36 | 5/14 (NCI-H1792, SW 900, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.12×** | +12.0 | 6e-31 | 13/14 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.21×** | +9.9 | 7e-21 | 12/14 (NCI-H1792, SW 900, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.24×** | +9.3 | 1e-18 | 12/14 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.13×** | +6.7 | 3e-09 | 7/14 (SW 900, Hs 766T, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.90×** | +5.7 | 1e-06 | 12/14 (NCI-H1792, SW 900, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +4.9 | 6e-05 | 10/14 (NCI-H1792, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.18×** | +4.7 | 1e-04 | 2/14 (SNU-423, SW 900) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.66×** | +4.4 | 5e-04 | 3/14 (SW 900, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.96×** | +4.1 | 0.002 | 11/14 (HEC-1-A, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.86×** | +3.7 | 0.008 | 11/14 (HEC-1-A, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.82×** | +3.6 | 0.012 | 10/14 (SW 900, SNU-423, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.48×** | +3.5 | 0.021 | 11/14 (A549, Panc 03.27, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.50×** | +3.4 | 0.024 | 12/14 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.67×** | +3.1 | 0.066 | 0/14 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.069 | 11/14 (CFPAC-1, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5713.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.509×** | -6.0 | 1e-06 | 12/14 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.530×** | -5.6 | 5e-06 | 12/14 (KATO III, BT-474, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.583×** | -4.8 | 3e-04 | 14/14 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.704× | -3.1 | 0.20 | 0/14 | two highest doses |  |
| [[Rifaximin (drug)]] 5 µM |  | 0.694× | -3.1 | 0.20 | 8/14 (HEC-1-A, NCI-H2347, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.707× | -3.1 | 0.20 | 1/14 (NCI-H1573) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5713. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 35.0 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 19.9× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 6.51× (z +9.4) | — |
| [[KATO III (line)]] | alt | 330 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -15.7) |
| [[NCI-H1573 (line)]] | alt | 270 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 6.86× (z +10.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.141× (z -10.8) |
| [[BT-474 (line)]] | alt | 273 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.109× (z -16.9) |
| [[SW 900 (line)]] | alt | 37.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.60× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 4.94× (z +9.0) | — |
| [[A549 (line)]] | wt | 372 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.96× (z +11.9) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 595 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 41.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 646 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 37.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.23× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 13.8 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.19 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 8.36 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.33 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.56 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.93 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.69 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.30 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.97 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.88 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.65 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 307 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.3 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.08 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 13.3 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.05 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.98 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 645 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.78 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.49 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.46 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.68 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.4 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.65 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.06 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 11.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5713), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGD4]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[KRT86]] | +0.59 | +0.57 / +0.52 | both halves | 1e-05 | same gene group; pathway: Formation of the cornified envelope; STRING 504; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[AHNAK]] | +0.58 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[DNAH5]] | +0.57 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[FSTL3]] | +0.53 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[LPP]] | +0.52 | +0.34 / +0.52 | both halves | 1e-04 |  |
| [[MAOA]] | +0.52 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[KRT80]] | +0.50 | +0.39 / +0.46 | both halves | 6e-05 | same gene group; pathway: Formation of the cornified envelope; STRING 561; ⚠ same locus (40.5 kb: neighbours can correlate without regulation) |
| [[TES]] | +0.49 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[CPNE1]] | +0.49 | +0.39 / +0.47 | both halves | 6e-05 |  |
| [[SUSD5]] | +0.49 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[ACTB]] | +0.48 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[CDV3]] | +0.48 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[ACOT9]] | +0.48 | +0.38 / +0.47 | both halves | 6e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABEP2]] | -0.49 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[LINC02210-CRHR1]] | -0.48 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[ZNRF1]] | -0.46 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[CRLF2]] | -0.46 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[ATAT1]] | -0.45 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[EVA1A-AS]] | -0.44 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[MRPS6]] | -0.43 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[NGLY1]] | -0.43 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[UPK1A-AS1]] | -0.42 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[ABCB9]] | -0.42 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[TMCC3]] | -0.42 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[TMEM144]] | -0.42 | -0.38 / -0.40 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT86]] | B | KRT86 activity raises KRT7's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 4.49× lower at baseline in the lines without KRT86 | 0.004 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[HDAC6]] | B | HDAC6 activity raises KRT7's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ABCC3]] | B | ABCC3 activity raises KRT7's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 3.40× lower at baseline in the lines without ABCC3 | 0.048 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[IGFBP3]] | B | IGFBP3 activity raises KRT7's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 2.19× lower at baseline in the lines without IGFBP3 | 0.078 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |
| [[GSDMC]] | C | GSDMC activity raises KRT7's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 11.29× lower at baseline in the lines without GSDMC | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1; co-absent with the target |
| [[KRT80]] | C | KRT80 activity raises KRT7's level | lines that do not express KRT80 (22) vs lines expressing it (28) | 3.86× lower at baseline in the lines without KRT80 | 0.006 | ⚠ within organs, on part of the lines; also absent: C19orf33, EPS8L2, SPNS2; co-absent with the target |
| [[KRT81]] | C | KRT81 activity raises KRT7's level | lines that do not express KRT81 (34) vs lines expressing it (16) | 3.41× lower at baseline in the lines without KRT81 | 0.008 | ⚠ within organs, on part of the lines; also absent: CARD11, ANXA8, PSG9; co-absent with the target |
| [[TMCC3]] | C | TMCC3 activity raises KRT7's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 3.97× lower at baseline in the lines without TMCC3 | 0.019 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4; co-absent with the target |
| [[CAPN8]] | C | CAPN8 activity raises KRT7's level | lines that do not express CAPN8 (35) vs lines expressing it (15) | 3.43× lower at baseline in the lines without CAPN8 | 0.036 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, ARHGEF38; co-absent with the target |
| [[SCEL]] | C | SCEL activity raises KRT7's level | lines that do not express SCEL (35) vs lines expressing it (15) | 4.21× lower at baseline in the lines without SCEL | 0.037 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 14, C 4. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCC3]] | B | KRT7 activity raises ABCC3's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 3.04× lower at baseline in the lines without KRT7 | 0.009 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3 |
| [[KRT86]] | B | KRT7 activity raises KRT86's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 3.65× lower at baseline in the lines without KRT7 | 0.009 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3 |
| [[ATIC]] | B | KRT7 activity lowers ATIC's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 1.45× higher at baseline in the lines without KRT7 | 0.011 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3 |
| [[RABGEF1P3]] | B | KRT7 activity raises RABGEF1P3's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 1.35× lower at baseline in the lines without KRT7 | 0.012 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3 |
| [[ANXA2]] | B | KRT7 activity raises ANXA2's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 1.52× lower at baseline in the lines without KRT7 | 0.026 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3 |
| [[UNC13D]] | B | KRT7 activity raises UNC13D's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 2.17× lower at baseline in the lines without KRT7 | 0.037 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3 |
| [[KRT8]] | B | KRT7 activity raises KRT8's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 1.85× lower at baseline in the lines without KRT7 | 0.045 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3 |
| [[TES]] | B | KRT7 activity raises TES's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 2.08× lower at baseline in the lines without KRT7 | 0.056 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3 |
| [[SLC26A2]] | B | KRT7 activity strengthens SLC26A2's drug response | lines that do not express KRT7 (32) vs lines expressing it (12) | the lines without KRT7 respond 0.67× as strongly (z diff +0.89); strongest at Panobinostat 0.5 µM: 1.30x vs 2.05x (z diff +2.2) | 0.065 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3; target measured in part of the lines; both ways; artifact flags |
| [[TMEM51]] | B | KRT7 activity raises TMEM51's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 1.54× lower at baseline in the lines without KRT7 | 0.082 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3 |
| [[ATIC]] | B | KRT7 activity strengthens ATIC's drug response | lines that do not express KRT7 (34) vs lines expressing it (14) | the lines without KRT7 respond 0.78× as strongly (z diff +0.62); strongest at Homoharringtonine 0.5 µM: 1.34x vs 2.22x (z diff +3.1) | 0.086 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3; target measured in part of the lines; both ways; artifact flags |
| [[SPSB1]] | B | KRT7 activity raises SPSB1's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 1.34× lower at baseline in the lines without KRT7 | 0.094 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3 |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.529). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.3, 19.3); signed map (16.4, 25.1). **Vector** length 57.6, 20.4% of its response variance represented; |z| ≥ 3 in 445 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +15.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +9.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.5 | +13.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.2 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +3.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.1 | +1.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.8 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.8 | +0.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -1.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.2 | -2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.2 | -3.1 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.1 | -0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -0.2 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -0.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | keratin 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:52,232,520-52,252,186 (+) |
| Ensembl biotype | protein_coding |
| Also known as | K7, CK7, CK-7, K2C7, SCL |
| Gene groups (HGNC) | Keratins, type II |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [P08729](https://www.uniprot.org/uniprotkb/P08729) (Keratin, type II cytoskeletal 7):

> Blocks interferon-dependent interphase and stimulates DNA synthesis in cells. Involved in the translational regulation of the human papillomavirus type 16 E7 mRNA (HPV16 E7).

**Summary**, from NCBI Gene [3855](https://www.ncbi.nlm.nih.gov/gene/3855):

> The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the simple epithelia lining the cavities of the internal organs and in the gland ducts and blood vessels. The genes encoding the type II cytokeratins are clustered in a …

**Accessions** — [HGNC:6445](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6445) · Entrez [3855](https://www.ncbi.nlm.nih.gov/gene/3855) · UniProt [P08729](https://www.uniprot.org/uniprotkb/P08729) · Ensembl [ENSG00000135480](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135480)

## Data

Gene col 5713: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5713); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5713, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5713]; `tensor/DDL_lfc|DDL_z.npy` [5713]; `embed/gene_vectors.npy` [5713]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5713 or target_col == 5713). Every well: [[KRT7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRT7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
