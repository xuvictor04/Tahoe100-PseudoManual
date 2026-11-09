---
symbol: "LMAN2"
type: "gene"
col: 9776
ensembl_id: "ENSG00000169223"
name: "lectin, mannose binding 2"
location: "5q35.3"
module: 42
arm: "+"
pooled_cpm: 78.53
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# LMAN2

*lectin, mannose binding 2* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.17× (z +12.4, q 2e-32, up in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.40× (z +8.1, q 1e-13, up in 36 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.581× (z -13.1, q 1e-36, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDOST]] (+0.75, fdr 7e-06), [[TMED10]] (+0.74, fdr 7e-06), [[PDIA3]] (+0.71, fdr 7e-06); moves opposite to [[CEP83]] (-0.53, fdr 1e-05), [[KRI1]] (-0.52, fdr 6e-05), [[MPHOSPH6]] (-0.51, fdr 3e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9776.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +12.4 | 2e-32 | 45/49 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +11.6 | 2e-28 | 37/41 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +8.1 | 1e-13 | 36/49 (BT-474, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +6.2 | 6e-08 | 32/45 (SNU-423, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.1 | 0.005 | 18/48 (HOP62, SW1417, …) | top dose only | position effect removed |
| [[Aliskiren (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.030 | 24/49 (A498, A-172, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~14% of this change | **1.23×** | +3.5 | 0.034 | 23/48 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.23×** | +3.4 | 0.041 | 23/48 (A-427, SNU-423, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.4 | 0.041 | 0/50 | inconsistent across doses |  |
| [[Zileuton (drug)]] 0.5 µM |  | **1.20×** | +3.2 | 0.089 | 17/48 (NCI-H2030, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9776.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.581×** | -13.1 | 1e-36 | 42/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.658×** | -6.9 | 2e-09 | 40/48 (KATO III, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.790×** | -5.7 | 2e-06 | 33/48 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.760×** | -4.7 | 4e-04 | 25/48 (AN3 CA, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.783×** | -4.2 | 0.003 | 30/48 (NCI-H1573, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.810×** | -3.5 | 0.047 | 21/47 (NCI-H1573, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.823×** | -3.3 | 0.067 | 21/48 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.817×** | -3.3 | 0.082 | 22/48 (SW 1088, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | 0.831× | -3.0 | 0.15 | 20/49 (A498, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9776. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 101 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -10.5) |
| [[A-172 (line)]] | wt | 94.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 74.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -10.3) |
| [[HOP62 (line)]] | alt | 69.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.14× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 80.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -11.4) |
| [[A498 (line)]] | wt | 85.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 48.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +11.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 96.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 104 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -14.8) |
| [[LOX-IMVI (line)]] | wt | 47.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +8.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 58.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 57.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 79.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +11.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 115 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.28× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.539× (z -10.8) |
| [[PANC-1 (line)]] | alt | 66.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +11.3) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 63.9 | 1 (1 ⚠) | 1 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.90× (z +9.8) ⚠ toxic; cell-cycle shift, explains ~90% of this change | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -11.4) |
| [[A-427 (line)]] | wt | 57.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +9.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 62.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.563× (z -9.1) |
| [[BT-474 (line)]] | alt | 67.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -9.2) |
| [[H4 (line)]] | wt | 149 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -14.8) |
| [[HS-578T (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -9.6) |
| [[HT-29 (line)]] | alt | 78.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 79.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -8.7) |
| [[J82 (line)]] | alt | 67.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 52.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +12.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -15.3) |
| [[SK-MEL-2 (line)]] | alt | 69.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 74.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Fostamatinib (disodium hexahydrate) (drug)]] 5 µM 0.0936× (z -9.8) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 158 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -13.0) |
| [[SW1417 (line)]] | alt | 73.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.572× (z -8.6) |
| [[SW480 (line)]] | alt | 74.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +10.0) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 71.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 81.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 79.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 79.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 98.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 71.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9776), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDOST]] | +0.75 | +0.75 / +0.71 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 600 |
| [[TMED10]] | +0.74 | +0.76 / +0.70 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 839 |
| [[PDIA3]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[OS9]] | +0.70 | +0.73 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 526 |
| [[HYOU1]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[SPCS2]] | +0.68 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[CALR]] | +0.66 | +0.78 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 513 |
| [[TMED2]] | +0.66 | +0.70 / +0.64 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 865 |
| [[RPN1]] | +0.66 | +0.69 / +0.57 | both halves | 9e-06 | pathway: Asparagine N-linked glycosylation; STRING 522 |
| [[PDIA6]] | +0.66 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[CANX]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 625 |
| [[DNAJB11]] | +0.65 | +0.67 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP83]] | -0.53 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[KRI1]] | -0.52 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[MPHOSPH6]] | -0.51 | -0.45 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises LMAN2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.716). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.0, -21.8); signed map (-56.0, 6.5). **Vector** length 101, 27.8% of its response variance represented; |z| ≥ 3 in 725 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.61 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.61 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.61 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +8.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +5.0 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.0 | +0.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -5.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.1 | -3.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.0 | -3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | lectin, mannose binding 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:177,315,805-177,351,840 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GP36B, VIP36; previously C5orf8 |
| Reactome | 7 pathways, smallest: Cargo concentration in the ER; COPII-mediated vesicle transport; ER to Golgi Anterograde Transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12907](https://www.uniprot.org/uniprotkb/Q12907) (Vesicular integral-membrane protein VIP36):

> Plays a role as an intracellular lectin in the early secretory pathway. Interacts with N-acetyl-D-galactosamine and high-mannose type glycans and may also bind to O-linked glycans. Involved in the transport and sorting of glycoproteins carrying high mannose-type glycans (By similarity).

**Summary**, from NCBI Gene [10960](https://www.ncbi.nlm.nih.gov/gene/10960):

> This gene encodes a type I transmembrane lectin that shuttles between the endoplasmic reticulum, the Golgi apparatus and the plasma membrane. The encoded protein binds high mannose type glycoproteins and may facilitate their sorting, trafficking and quality control. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:16986](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16986) · Entrez [10960](https://www.ncbi.nlm.nih.gov/gene/10960) · UniProt [Q12907](https://www.uniprot.org/uniprotkb/Q12907) · Ensembl [ENSG00000169223](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169223)

## Data

Gene col 9776: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9776); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9776, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9776]; `tensor/DDL_lfc|DDL_z.npy` [9776]; `embed/gene_vectors.npy` [9776]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9776 or target_col == 9776). Every well: [[LMAN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMAN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
