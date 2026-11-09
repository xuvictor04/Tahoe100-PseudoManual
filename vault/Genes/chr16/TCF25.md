---
symbol: "TCF25"
type: "gene"
col: 6478
ensembl_id: "ENSG00000141002"
name: "TCF25 ribosome quality control complex subunit"
location: "16q24.3"
module: 21
arm: "+"
pooled_cpm: 126.52
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# TCF25

*TCF25 ribosome quality control complex subunit* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.31× (z +5.7, q 5e-06, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.487× (z -15.2, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK3]] (+0.68, fdr 7e-06), [[TMEM91]] (+0.61, fdr 1e-05), [[TTC36-AS1]] (+0.60, fdr 2e-05); moves opposite to [[MINPP1]] (-0.60, fdr 1e-05), [[SDHAF3]] (-0.60, fdr 1e-05), [[PHB1]] (-0.59, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6478.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +5.7 | 5e-06 | 32/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.18× | +4.9 | 3e-04 | 24/48 (NCI-H2030, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +4.7 | 5e-04 | 26/48 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.34×** | +4.3 | 0.002 | 34/48 (AsPC-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.2 | 0.003 | 22/48 (HS-578T, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.22×** | +4.2 | 0.003 | 26/49 (NCI-H460, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.005 | 30/48 (LS 180, Hs 766T, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.010 | 24/49 (COLO 205, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.19× | +3.7 | 0.012 | 21/49 (A498, HEC-1-A, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.014 | 28/48 (HS-578T, LS 180, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.030 | 25/49 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.030 | 21/48 (RKO, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.041 | 21/48 (A498, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.057 | 18/49 (PANC-1, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.2 | 0.061 | 20/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.084 | 20/48 (Hs 766T, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6478.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.487×** | -15.2 | 0e+00 | 46/48 (NCI-H2030, HS-578T, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.488×** | -15.1 | 0e+00 | 45/48 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.508×** | -14.3 | 8e-44 | 45/48 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.644×** | -9.3 | 3e-18 | 44/48 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.737×** | -6.4 | 2e-08 | 35/48 (A498, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.579×** | -6.0 | 2e-07 | 42/49 (A498, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.822×** | -5.8 | 5e-07 | 24/48 (SNU-423, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.602×** | -5.6 | 2e-06 | 36/49 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.835× | -5.4 | 5e-06 | 22/48 (A-172, HS-578T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.881× | -3.8 | 0.009 | 15/48 (A498, NCI-H2030, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.843× | -3.6 | 0.017 | 22/48 (KATO III, RKO, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~59% of this change | 0.855× | -3.2 | 0.070 | 19/47 (A-172, HCT15, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6478. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 103 | 5 (5 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.20× (z +11.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.402× (z -13.5) |
| [[A498 (line)]] | wt | 188 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.367× (z -16.9) |
| [[NCI-H2030 (line)]] | alt | 194 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +11.5) ⚠ cell-cycle shift, explains ~22% of this change | [[Belinostat (drug)]] 5 µM 0.327× (z -16.4) |
| [[A-172 (line)]] | wt | 153 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.413× (z -13.5) |
| [[HS-578T (line)]] | alt | 162 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.344× (z -15.6) |
| [[NCI-H1792 (line)]] | alt | 125 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.433× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 103 | 1 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.09× (z +8.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.456× (z -9.5) |
| [[PANC-1 (line)]] | alt | 95.7 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.344× (z -14.3) |
| [[SK-MEL-2 (line)]] | alt | 113 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -15.3) |
| [[A-427 (line)]] | wt | 113 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.407× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 98.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.363× (z -12.8) |
| [[H4 (line)]] | wt | 173 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.277× (z -13.6) |
| [[HCT15 (line)]] | alt | 171 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.381× (z -10.7) |
| [[Hs 766T (line)]] | wt | 123 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.467× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 136 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.351× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 108 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.420× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 143 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.477× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 70.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.426× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 82.5 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.438× (z -9.4) |
| [[SNU-1 (line)]] | wt | 184 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.346× (z -12.7) |
| [[SNU-423 (line)]] | alt | 114 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.403× (z -11.1) |
| [[SW 900 (line)]] | alt | 121 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.423× (z -10.6) |
| [[A549 (line)]] | wt | 101 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.422× (z -10.7) |
| [[HOP62 (line)]] | alt | 138 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.508× (z -10.5) |
| [[HT-29 (line)]] | alt | 139 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.529× (z -9.3) |
| [[J82 (line)]] | alt | 106 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.483× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 122 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.397× (z -10.5) |
| [[SW 1088 (line)]] | alt | 167 | 0 | 2 | — | [[Carbamazepine (drug)]] 0.5 µM 0.0612× (z -14.0) |
| [[BT-474 (line)]] | alt | 125 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.461× (z -9.9) |
| [[C32 (line)]] | wt | 144 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.454× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 128 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.493× (z -8.9) |
| [[COLO 205 (line)]] | alt | 160 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.470× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 194 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.532× (z -9.2) |
| [[NCI-H596 (line)]] | alt | 133 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.137× (z -10.4) |
| [[SHP-77 (line)]] | alt | 74.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.1) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[AN3 CA (line)]] | alt | 126 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 111 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 76.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 129 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 109 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 140 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 111 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 163 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 143 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 98.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6478), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK3]] | +0.68 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[TMEM91]] | +0.61 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[TTC36-AS1]] | +0.60 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[CIRBP]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[HSPA2-AS1]] | +0.59 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[EAF1-AS1]] | +0.57 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[ASB14]] | +0.56 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[GTF2IRD2]] | +0.56 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[GPAT4-AS1]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[HOOK2]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CCDC65]] | +0.55 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ZRANB2-AS1]] | +0.55 | +0.46 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MINPP1]] | -0.60 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[SDHAF3]] | -0.60 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[PHB1]] | -0.59 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[ICMT]] | -0.59 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[PGAM1]] | -0.58 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[VANGL1]] | -0.57 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[GPAM]] | -0.56 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[ABHD10]] | -0.54 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[WRNIP1]] | -0.53 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[C1QBP]] | -0.53 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[NME1]] | -0.53 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[GOT2]] | -0.53 | -0.55 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TCF25's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.508). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.1, 28.3); signed map (-3.9, 1.8). **Vector** length 122, 37.7% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +9.1 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.7 | +5.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +5.2 | +4.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.0 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +4.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +3.7 | +3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.7 | +3.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.1 | -5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.5 | -2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.0 | -9.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.8 | -6.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.0 | -5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -6.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.2 | -1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | TCF25 ribosome quality control complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:89,873,570-89,913,627 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Nulp1, KIAA1049 |
| Reactome | 3 pathways, smallest: Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide; Ribosome-associated quality control; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQ70](https://www.uniprot.org/uniprotkb/Q9BQ70) (Ribosome quality control complex subunit TCF25):

> Component of the ribosome quality control complex (RQC), a ribosome-associated complex that mediates ubiquitination and extraction of incompletely synthesized nascent chains for proteasomal degradation. In the RQC complex, required to promote formation of 'Lys-48'-linked polyubiquitin chains during ubiquitination of incompletely synthesized proteins by LTN1. May negatively regulate the calcineurin-NFAT signaling cascade by suppressing the activity of transcription factor NFATC4 (By similarity). …

**Summary**, from NCBI Gene [22980](https://www.ncbi.nlm.nih.gov/gene/22980):

> TCF25 is a member of the basic helix-loop-helix (bHLH) family of transcription factors that are important in embryonic development (Steen and Lindholm, 2008 [PubMed 18068114]).[supplied by OMIM, Sep 2008]

**Accessions** — [HGNC:29181](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29181) · Entrez [22980](https://www.ncbi.nlm.nih.gov/gene/22980) · UniProt [Q9BQ70](https://www.uniprot.org/uniprotkb/Q9BQ70) · Ensembl [ENSG00000141002](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141002)

## Data

Gene col 6478: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6478); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6478, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6478]; `tensor/DDL_lfc|DDL_z.npy` [6478]; `embed/gene_vectors.npy` [6478]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6478 or target_col == 6478). Every well: [[TCF25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCF25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
