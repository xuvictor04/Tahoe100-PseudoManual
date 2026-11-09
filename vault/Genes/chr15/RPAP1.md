---
symbol: "RPAP1"
type: "gene"
col: 2401
ensembl_id: "ENSG00000103932"
name: "RNA polymerase II associated protein 1"
location: "15q15.1"
module: 114
arm: "+"
pooled_cpm: 24.33
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 10
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# RPAP1

*RNA polymerase II associated protein 1* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.45× (z +11.4, q 3e-27, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.598× (z -10.8, q 1e-24, down in 35 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.689× (z -8.2, q 8e-14, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABRAXAS2]] (+0.75, fdr 7e-06), [[ZC3HC1]] (+0.75, fdr 7e-06), [[MAU2]] (+0.68, fdr 7e-06); moves opposite to [[MGAT4A]] (-0.65, fdr 1e-05), [[TWSG1]] (-0.62, fdr 2e-05), [[C12orf75]] (-0.61, fdr 1e-05).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2401.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +11.4 | 3e-27 | 30/47 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +8.1 | 2e-13 | 27/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +7.0 | 4e-10 | 26/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +6.7 | 3e-09 | 25/47 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +6.4 | 2e-08 | 21/48 (NCI-H2347, NCI-H2030, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.33×** | +5.8 | 5e-07 | 20/47 (KATO III, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +5.6 | 2e-06 | 27/48 (HT-29, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +5.4 | 6e-06 | 20/47 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +5.3 | 7e-06 | 21/48 (A498, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +5.3 | 8e-06 | 19/48 (NCI-H460, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.7 | 1e-04 | 19/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.6 | 2e-04 | 19/48 (NCI-H1573, A498, …) | rises with dose | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.002 | 9/46 (MIA PaCa-2, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.13× | +3.8 | 0.005 | 14/48 (NCI-H1792, AsPC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.18× | +3.7 | 0.008 | 12/47 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.023 | 15/48 (Panc 03.27, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2401.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.598×** | -10.8 | 1e-24 | 35/47 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.689×** | -8.2 | 8e-14 | 30/48 (KATO III, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.684×** | -7.7 | 2e-12 | 22/39 (NCI-H23, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.746×** | -6.4 | 2e-08 | 27/48 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.768×** | -5.8 | 7e-07 | 21/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.769×** | -5.8 | 8e-07 | 24/48 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.788×** | -5.2 | 1e-05 | 19/47 (hTERT-HPNE, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.799×** | -4.9 | 6e-05 | 21/44 (SK-MEL-2, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.715×** | -3.9 | 0.007 | 14/30 (HOP62, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.887× | -3.8 | 0.010 | 16/48 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.723×** | -3.7 | 0.010 | 9/48 (SNU-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.844× | -3.6 | 0.016 | 15/34 (HEC-1-A, NCI-H1792, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.855× | -3.4 | 0.026 | 11/48 (NCI-H460, A-427, …) | rises with dose |  |
| [[Penfluridol (drug)]] 5 µM |  | 0.853× | -3.4 | 0.032 | 11/47 (J82, RPMI-7951, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.859× | -3.3 | 0.032 | 12/48 (SW480, NCI-H2030, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2401. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 25.9 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -12.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 27.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.375× (z -11.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 25.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 21.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -9.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 37.2 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.25× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.323× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 31.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 28.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.376× (z -10.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 19.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -12.8) |
| [[AsPC-1 (line)]] | alt | 12.9 | 0 | 1 | — | [[Vismodegib (drug)]] 0.5 µM 0.167× (z -10.7) |
| [[C32 (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 25.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +11.9) | — |
| [[HS-578T (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.220× (z -8.8) ⚠ toxic |
| [[HT-29 (line)]] | alt | 21.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 22.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -15.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.475× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2401), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABRAXAS2]] | +0.75 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[ZC3HC1]] | +0.75 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[MAU2]] | +0.68 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[MRPL38]] | +0.68 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[ALKBH1]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[C12orf43]] | +0.66 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[NSRP1]] | +0.66 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[NAIF1]] | +0.65 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[DOHH]] | +0.65 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[SART3]] | +0.65 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[MRM3]] | +0.65 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[MTG2]] | +0.64 | +0.67 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGAT4A]] | -0.65 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[TWSG1]] | -0.62 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[C12orf75]] | -0.61 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[LAPTM4A]] | -0.60 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[PTP4A2]] | -0.59 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[GTF2IP4]] | -0.58 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ATP8A1]] | -0.58 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[CBX1]] | -0.57 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[NR3C2]] | -0.57 | -0.50 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises RPAP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.2, 7.1); signed map (-3.1, -15.2). **Vector** length 99.6, 21.4% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.4 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +11.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +8.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.9 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +3.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.0 | +3.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.1 | -10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.6 | -7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.9 | -4.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.5 | -5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.4 | -5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -2.9 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.4 | -1.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase II associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:41,517,176-41,544,269 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP727M111, KIAA1403, MGC858, FLJ12732 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWH6](https://www.uniprot.org/uniprotkb/Q9BWH6) (RNA polymerase II-associated protein 1):

> Forms an interface between the RNA polymerase II enzyme and chaperone/scaffolding protein, suggesting that it is required to connect RNA polymerase II to regulators of protein complex formation. Required for interaction of the RNA polymerase II complex with acetylated histone H3.

**Summary**, from NCBI Gene [26015](https://www.ncbi.nlm.nih.gov/gene/26015):

> This protein forms part of the RNA polymerase II (RNAPII) enzyme complex and may recruit RNAPII to chromatin through its interaction with acetylated histones. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:24567](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24567) · Entrez [26015](https://www.ncbi.nlm.nih.gov/gene/26015) · UniProt [Q9BWH6](https://www.uniprot.org/uniprotkb/Q9BWH6) · Ensembl [ENSG00000103932](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103932)

## Data

Gene col 2401: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2401); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2401, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2401]; `tensor/DDL_lfc|DDL_z.npy` [2401]; `embed/gene_vectors.npy` [2401]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2401 or target_col == 2401). Every well: [[RPAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
