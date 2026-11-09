---
symbol: "PLXNB3-AS1"
type: "gene"
col: 13863
ensembl_id: "ENSG00000232725"
name: "PLXNB3 antisense RNA 1"
location: "Xq28"
module: 46
arm: "+"
pooled_cpm: 3.15
n_lines_expressing: 39
n_dd_up: 5
n_dd_down: 6
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# PLXNB3-AS1

*PLXNB3 antisense RNA 1* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.50× (z +13.4, q 6e-38, up in 15 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.520× (z -6.7, q 2e-08, down in 16 of 34 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEIL1]] (+0.60, fdr 1e-04), [[LINC01134]] (+0.56, fdr 1e-04), [[LINC00649]] (+0.56, fdr 2e-04); moves opposite to [[PUSL1]] (-0.49, fdr 6e-04), [[SLC1A1]] (-0.48, fdr 3e-04), [[NPHP4]] (-0.48, fdr 3e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HOTAIR]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NNT-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13863.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.50×** | +13.4 | 6e-38 | 15/24 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.91×** | +10.6 | 1e-23 | 2/6 (SW480, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.38×** | +8.9 | 9e-17 | 10/16 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +7.3 | 4e-11 | 3/9 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.26×** | +3.4 | 0.086 | 9/32 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.81× | +3.2 | 0.12 | 0/8 | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.35× | +3.1 | 0.13 | 3/22 (LOX-IMVI, COLO 205, …) | inconsistent across doses | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.35× | +3.1 | 0.13 | 2/19 (SW480, HT-29) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.34× | +3.0 | 0.16 | 5/26 (HOP62, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13863.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.520×** | -6.7 | 2e-08 | 16/34 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.565×** | -5.8 | 1e-06 | 15/31 (COLO 205, SW480, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.655×** | -4.3 | 0.002 | 18/32 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.657×** | -4.3 | 0.002 | 15/29 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.705×** | -3.6 | 0.041 | 6/33 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.725×** | -3.3 | 0.096 | 13/32 (SW480, SNU-423, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.737× | -3.0 | 0.22 | 11/28 (PANC-1, J82, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13863. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.02 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0867× (z -13.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[COLO 205 (line)]] | alt | 8.14 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0428× (z -10.8) |
| [[Hs 766T (line)]] | wt | 6.17 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Gallic acid (drug)]] 0.05 µM 0.0853× (z -8.9) |
| [[LS 180 (line)]] | wt | 6.39 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.1000× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H460 (line)]] | wt | 3.28 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0727× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 6.87 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0756× (z -9.4) |
| [[SNU-423 (line)]] | alt | 6.82 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 5.33 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW480 (line)]] | alt | 8.25 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.238× (z -9.0) |
| [[A-172 (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.624 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.557 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.634 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.790 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.828 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.752 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.553 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.997 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.647 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.974 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.960 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.627 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13863), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEIL1]] | +0.60 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[LINC01134]] | +0.56 | +0.48 / +0.33 | both halves | 1e-04 |  |
| [[LINC00649]] | +0.56 | +0.47 / +0.31 | both halves | 2e-04 |  |
| [[DHX38]] | +0.55 | +0.36 / +0.43 | both halves | 1e-04 |  |
| [[GLDN]] | +0.54 | +0.52 / +0.30 | both halves | 2e-04 |  |
| [[MYH7B]] | +0.51 | +0.37 / +0.36 | both halves | 9e-05 |  |
| [[BCAR3-AS1]] | +0.51 | +0.43 / +0.31 | both halves | 2e-04 | same gene group |
| [[ALKBH6]] | +0.51 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[PGAP4]] | +0.50 | +0.51 / +0.25 | both halves | 4e-04 |  |
| [[ACCS]] | +0.50 | +0.43 / +0.27 | both halves | 3e-04 |  |
| [[SH2B1]] | +0.50 | +0.34 / +0.44 | both halves | 1e-04 |  |
| [[NNT]] | +0.49 | +0.23 / +0.39 | both halves | 5e-04 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUSL1]] | -0.49 | -0.37 / -0.22 | both halves | 6e-04 |  |
| [[SLC1A1]] | -0.48 | -0.52 / -0.28 | both halves | 3e-04 |  |
| [[NPHP4]] | -0.48 | -0.27 / -0.28 | both halves | 3e-04 |  |
| [[NAA10]] ⚠ | -0.48 | -0.40 / -0.14 | ⚠ not reproduced | 0.002 | ⚠ in the vector space only through flagged drug-doses |
| [[SPTSSA]] | -0.47 | -0.19 / -0.50 | ⚠ not reproduced | 8e-04 |  |
| [[RPS6KA5]] | -0.47 | -0.31 / -0.34 | both halves | 2e-04 |  |
| [[UNC13B]] | -0.46 | -0.27 / -0.37 | both halves | 3e-04 |  |
| [[GPRIN1]] | -0.45 | -0.22 / -0.37 | both halves | 6e-04 |  |
| [[TXNL4A]] | -0.45 | -0.34 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOTAIR]] | B | HOTAIR activity raises PLXNB3-AS1's level | lines that do not express HOTAIR (27) vs lines expressing it (23) | 1.57× lower at baseline in the lines without HOTAIR | 0.020 | ⚠ within organs, on part of the lines; also absent: CES1, DOK5, ANKRD20A9P |
| [[HDAC6]] | B | HDAC6 activity raises PLXNB3-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NNT-AS1]] | B | PLXNB3-AS1 activity strengthens NNT-AS1's drug response | lines that do not express PLXNB3-AS1 (10) vs lines expressing it (32) | the lines without PLXNB3-AS1 respond 0.66× as strongly (z diff +1.53); strongest at Belinostat 5 µM: 0.45x vs 0.31x (z diff +2.9) | 0.042 | ⚠ within organs, on part of the lines; also absent: CA9; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.437). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (1.5, 29.8); signed map (37.1, -13.9). **Vector** length 39.4, 5.23% of its response variance represented; |z| ≥ 3 in 726 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +7.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.6 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +0.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -5.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.6 | -4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -6.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -1.2 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -1.0 |
|  | [[Malotilate (drug)]] 5 µM |  | -0.8 | -1.0 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.8 | -2.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | PLXNB3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xq28 — chrX:153,735,626-153,766,478 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40454](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40454) · Entrez [102723591](https://www.ncbi.nlm.nih.gov/gene/102723591) · Ensembl [ENSG00000232725](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232725)

## Data

Gene col 13863: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13863); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13863, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13863]; `tensor/DDL_lfc|DDL_z.npy` [13863]; `embed/gene_vectors.npy` [13863]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13863 or target_col == 13863). Every well: [[PLXNB3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLXNB3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
