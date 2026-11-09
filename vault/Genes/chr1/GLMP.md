---
symbol: "GLMP"
type: "gene"
col: 12649
ensembl_id: "ENSG00000198715"
name: "glycosylated lysosomal membrane protein"
location: "1q22"
module: 122
arm: "+"
pooled_cpm: 7.17
n_lines_expressing: 46
n_dd_up: 5
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# GLMP

*glycosylated lysosomal membrane protein* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.26× (z +9.5, q 2e-18, up in 20 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.51× (z +6.8, q 2e-09, up in 21 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.570× (z -6.5, q 5e-08, down in 23 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNASE2]] (+0.66, fdr 7e-06), [[CTSA]] (+0.66, fdr 7e-06), [[SPNS1]] (+0.66, fdr 1e-05); moves opposite to [[CPSF3]] (-0.55, fdr 3e-05), [[RAN]] (-0.49, fdr 6e-05), [[SRPK1]] (-0.49, fdr 1e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ARMCX1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CSAG1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12649.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +9.5 | 2e-18 | 20/30 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +9.0 | 6e-17 | 11/15 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +6.8 | 2e-09 | 10/19 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +6.8 | 2e-09 | 21/43 (C32, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +4.2 | 0.003 | 11/34 (J82, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.31× | +3.1 | 0.16 | 9/42 (C32, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12649.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.570×** | -6.5 | 5e-08 | 23/41 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.576×** | -6.1 | 3e-07 | 22/40 (SW 900, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.634×** | -5.2 | 3e-05 | 18/42 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.656×** | -4.8 | 2e-04 | 17/37 (NCI-H23, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.668×** | -4.6 | 4e-04 | 17/42 (LoVo, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.687×** | -4.1 | 0.004 | 15/41 (HT-29, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.702×** | -4.1 | 0.004 | 16/42 (KATO III, C32, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.712×** | -3.7 | 0.017 | 13/41 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.733×** | -3.4 | 0.039 | 14/41 (hTERT-HPNE, NCI-H2030, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.749×** | -3.3 | 0.054 | 11/42 (RKO, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.764× | -3.1 | 0.11 | 10/42 (AN3 CA, A-172, …) | top dose only | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12649. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 7.21 | 0 | 2 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0850× (z -8.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.0814× (z -8.6) |
| [[A549 (line)]] | wt | 4.73 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0909× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 9.21 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 3.73 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0913× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 6.77 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -8.5) |
| [[KATO III (line)]] | alt | 4.51 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0490× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -10.3) ⚠ cell-cycle shift, explains ~10% of this change |
| [[NCI-H23 (line)]] | alt | 5.26 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0809× (z -9.5) |
| [[A-172 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.751 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.773 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.634 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12649), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNASE2]] | +0.66 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[CTSA]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[SPNS1]] | +0.66 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[NPC2]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[HEXA]] | +0.63 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[ATP6AP1]] | +0.63 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[CTSF]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[NEU1]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ASAH1]] | +0.61 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[GM2A]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[VAT1]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[GNPTG]] | +0.60 | +0.50 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF3]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[RAN]] | -0.49 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[SRPK1]] | -0.49 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[CTPS1]] | -0.48 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[HNRNPAB]] | -0.48 | -0.38 / -0.53 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARMCX1]] | B | ARMCX1 activity raises GLMP's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 1.52× lower at baseline in the lines without ARMCX1 | 0.023 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1 |
| [[CTSF]] | B | CTSF activity raises GLMP's level | lines that do not express CTSF (16) vs lines expressing it (34) | 1.28× lower at baseline in the lines without CTSF | 0.066 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, LINC01725, BVES |
| [[RRAGD]] | B | RRAGD activity raises GLMP's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 1.26× lower at baseline in the lines without RRAGD | 0.0998 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSAG1]] | C | GLMP activity lowers CSAG1's level | lines that do not express GLMP (4) vs lines expressing it (46) | 2.35× higher at baseline in the lines without GLMP | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000255031, SMAD7, TCIRG1 |

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.746). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.7, -18.4); signed map (-24.5, -3.0). **Vector** length 54.9, 8.17% of its response variance represented; |z| ≥ 3 in 736 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.9 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +9.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +6.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.1 | +2.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.7 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +2.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.3 | -4.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.2 | -6.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | glycosylated lysosomal membrane protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:156,290,089-156,295,689 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC31963, NCU-G1, lnc-UCID; previously C1orf85 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWB7](https://www.uniprot.org/uniprotkb/Q8WWB7) (Glycosylated lysosomal membrane protein):

> Required to protect lysosomal transporter MFSD1 from lysosomal proteolysis and for MFSD1 lysosomal localization.

**Summary**, from NCBI Gene [112770](https://www.ncbi.nlm.nih.gov/gene/112770):

> Involved in positive regulation of transcription by RNA polymerase II. Located in cytosol; lysosome; and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29436](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29436) · Entrez [112770](https://www.ncbi.nlm.nih.gov/gene/112770) · UniProt [Q8WWB7](https://www.uniprot.org/uniprotkb/Q8WWB7) · Ensembl [ENSG00000198715](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198715)

## Data

Gene col 12649: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12649); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12649, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12649]; `tensor/DDL_lfc|DDL_z.npy` [12649]; `embed/gene_vectors.npy` [12649]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12649 or target_col == 12649). Every well: [[GLMP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLMP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
