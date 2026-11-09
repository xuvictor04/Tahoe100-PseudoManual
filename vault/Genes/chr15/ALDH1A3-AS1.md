---
symbol: "ALDH1A3-AS1"
type: "gene"
col: 15216
ensembl_id: "ENSG00000259583"
name: "ALDH1A3 antisense RNA 1"
location: "15q26.3"
module: 46
arm: "+"
pooled_cpm: 2.72
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# ALDH1A3-AS1

*ALDH1A3 antisense RNA 1* — 15q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.21× (z +10.3, q 3e-22, up in 2 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.87× (z +8.2, q 6e-14, up in 16 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.565× (z -5.3, q 9e-05, down in 18 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.217×; ⚠ cell-cycle shift, explains ~24% of this change).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRK1]] (+0.67, fdr 1e-05, ⚠ same locus), [[CDNF]] (+0.67, fdr 1e-05), [[IDNK]] (+0.60, fdr 4e-05), [[MRM1]] (+0.60, fdr 3e-05); moves opposite to [[KIAA0513]] (-0.53, fdr 4e-04), [[COPE]] (-0.50, fdr 1e-04), [[CHEK2]] (-0.48, fdr 3e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ALDH1A3]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[PH-797804 (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15216.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.21×** | +10.3 | 3e-22 | 2/3 (PANC-1, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.96×** | +10.0 | 6e-21 | 12/18 (LOX-IMVI, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +8.2 | 6e-14 | 16/30 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +7.0 | 3e-10 | 2/5 (PANC-1, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +6.2 | 8e-08 | 9/41 (KATO III, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +3.5 | 0.036 | 3/14 (LS 180, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.5 | 0.036 | 5/29 (AsPC-1, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.4 | 0.043 | 1/16 (LS 180) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.39× | +3.0 | 0.15 | 0/30 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15216.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.217×; ⚠ cell-cycle shift, explains ~24% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.565×** | -5.3 | 9e-05 | 18/39 (A498, RKO, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.658×** | -3.8 | 0.028 | 10/39 (SW48, SNU-423, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.747×** | -3.8 | 0.028 | 14/32 (PANC-1, HEC-1-A, …) | rises with dose | composition shift |
| [[Artesunate (drug)]] 0.5 µM |  | 0.709× | -3.2 | 0.22 | 2/41 (SNU-423, SW48) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.714× | -3.1 | 0.22 | 14/44 (NCI-H1792, Panc 03.27, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15216. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.94 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -9.7) ⚠ cell-cycle shift, explains ~24% of this change |
| [[A-172 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.990 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.899 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.922 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.969 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.907 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15216), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 9 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRK1]] | +0.67 | +0.68 / +0.51 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CDNF]] | +0.67 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[IDNK]] | +0.60 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[MRM1]] | +0.60 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[ZNF514]] | +0.59 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[ABHD15]] | +0.59 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[VSIG10]] | +0.58 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[PCMTD1-DT]] | +0.57 | +0.45 / +0.36 | both halves | 1e-04 |  |
| [[NINJ2]] | +0.57 | +0.40 / +0.36 | both halves | 1e-04 |  |
| [[TP53TG5]] | +0.57 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[RNF32]] | +0.57 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[HOTAIR]] | +0.56 | +0.34 / +0.45 | both halves | 1e-04 |  |
| [[TYSND1]] | +0.56 | +0.39 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA0513]] | -0.53 | -0.25 / -0.49 | both halves | 4e-04 |  |
| [[COPE]] | -0.50 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[CHEK2]] | -0.48 | -0.49 / -0.26 | both halves | 3e-04 |  |
| [[MAGT1]] | -0.48 | -0.37 / -0.39 | both halves | 7e-05 |  |
| [[STAM2]] | -0.48 | -0.34 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALDH1A3]] | B | ALDH1A3 activity raises ALDH1A3-AS1's level | lines that do not express ALDH1A3 (20) vs lines expressing it (30) | 1.36× lower at baseline in the lines without ALDH1A3 | 0.002 | ⚠ within organs, on part of the lines; also absent: SHROOM4, ENSG00000232386, ADAMTS16 |
| [[HDAC6]] | B | HDAC6 activity raises ALDH1A3-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GCAWKR]] | B | GCAWKR activity raises ALDH1A3-AS1's level | lines that do not express GCAWKR (20) vs lines expressing it (30) | 1.24× lower at baseline in the lines without GCAWKR | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000232386, IL31RA, BEX2 |
| [[LRRK1]] | B | LRRK1 activity raises ALDH1A3-AS1's level | lines that do not express LRRK1 (10) vs lines expressing it (40) | 1.76× lower at baseline in the lines without LRRK1 | 0.074 | ⚠ within organs, on part of the lines; also absent: HRH1, ALS2CL, CTSZ; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[PH-797804 (drug)]] 0.05 µM | C | ALDH1A3-AS1's natural level lowers the cells' numbers under PH-797804 0.05 µM (makes them more sensitive) | ALDH1A3-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.285 over the table, 0.045 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | ALDH1A3-AS1's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | ALDH1A3-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.491 over the table, 0.094 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.514). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (3.7, 22.0); signed map (35.5, -16.1). **Vector** length 37.8, 3.92% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +10.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.8 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +2.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.1 | +1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +1.8 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -1.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -1.4 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.0 | -1.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ALDH1A3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q26.3 — chr15:100,892,343-100,919,391 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55416](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55416) · Entrez [101927751](https://www.ncbi.nlm.nih.gov/gene/101927751) · Ensembl [ENSG00000259583](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259583)

## Data

Gene col 15216: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15216); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15216, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15216]; `tensor/DDL_lfc|DDL_z.npy` [15216]; `embed/gene_vectors.npy` [15216]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15216 or target_col == 15216). Every well: [[ALDH1A3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALDH1A3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
