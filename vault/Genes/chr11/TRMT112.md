---
symbol: "TRMT112"
type: "gene"
col: 10340
ensembl_id: "ENSG00000173113"
name: "tRNA methyltransferase activator subunit 11-2"
location: "11q13.1"
module: 131
arm: "+"
pooled_cpm: 50.95
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# TRMT112

*tRNA methyltransferase activator subunit 11-2* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.51× (z +7.0, q 2e-09, up in 46 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 2.61× (z +3.8, q 0.018, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (CHP-212 0.0662×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFAB1]] (+0.80, fdr 7e-06), [[RPS15]] (+0.79, fdr 7e-06, ⚠ RPS15 in the vector space only through flagged drug-doses), [[RPS23]] (+0.74, fdr 7e-06), [[CHCHD2]] (+0.74, fdr 7e-06); moves opposite to [[EIF4G2]] (-0.62, fdr 1e-05), [[PNPO]] (-0.61, fdr 1e-05), [[SEPTIN8]] (-0.56, fdr 3e-05).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ESRP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10340.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.51×** | +7.0 | 2e-09 | 46/46 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.41×** | +4.7 | 8e-04 | 35/41 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.03×** | +3.9 | 0.016 | 41/47 (NCI-H1573, NCI-H460, …) | top dose only | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.61×** | +3.8 | 0.018 | 46/48 (LoVo, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.56×** | +3.7 | 0.018 | 45/47 (A-427, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +3.7 | 0.018 | 40/47 (SW 900, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.92×** | +3.6 | 0.025 | 39/46 (HS-578T, RPMI-7951, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.22×** | +3.6 | 0.025 | 32/48 (PANC-1, BT-474, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **2.28×** | +3.3 | 0.066 | 42/48 (J82, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.79×** | +3.2 | 0.066 | 36/48 (HOP62, KATO III, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.26×** | +3.2 | 0.066 | 42/47 (SNU-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **2.21×** | +3.1 | 0.078 | 41/48 (C32, HEC-1-A, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (CHP-212 0.0662×; ⚠ cell-cycle shift, explains ~0% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10340. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 45.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.67× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[CHP-212 (line)]] | wt | 40.2 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0662× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 35.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.98× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 26.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.85× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H460 (line)]] | wt | 26.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.77× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 65.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 54.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10340), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 13 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFAB1]] | +0.80 | +0.76 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[RPS15]] ⚠ | +0.79 | +0.80 / +0.76 | both halves | 7e-06 | pathway: Eukaryotic Translation Termination; STRING 854; ⚠ in the vector space only through flagged drug-doses |
| [[RPS23]] | +0.74 | +0.72 / +0.72 | both halves | 7e-06 | pathway: Eukaryotic Translation Termination; STRING 834 |
| [[CHCHD2]] | +0.74 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[RPL38]] | +0.73 | +0.75 / +0.68 | both halves | 7e-06 | pathway: Eukaryotic Translation Termination |
| [[RPS10]] | +0.72 | +0.69 / +0.70 | both halves | 7e-06 | pathway: Eukaryotic Translation Termination |
| [[RPL8]] ⚠ | +0.72 | +0.69 / +0.67 | both halves | 7e-06 | pathway: Eukaryotic Translation Termination; ⚠ in the vector space only through flagged drug-doses |
| [[RPS21]] | +0.71 | +0.63 / +0.70 | both halves | 7e-06 | pathway: Eukaryotic Translation Termination; STRING 849 |
| [[NDUFA3]] | +0.70 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[SNHG25]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[FKBP2]] ⚠ | +0.69 | +0.70 / +0.65 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS13]] ⚠ | +0.68 | +0.65 / +0.67 | both halves | 7e-06 | pathway: Eukaryotic Translation Termination; STRING 846; ⚠ in the vector space only through flagged drug-doses |
| [[RPS11]] | +0.68 | +0.69 / +0.64 | both halves | 7e-06 | pathway: Eukaryotic Translation Termination; STRING 844 |
| [[RPL36A]] | +0.66 | +0.55 / +0.70 | both halves | 1e-05 | pathway: Eukaryotic Translation Termination |
| [[RPS29]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 | pathway: Eukaryotic Translation Termination |
| [[RPL32]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 | pathway: Eukaryotic Translation Termination |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.62 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[PNPO]] | -0.61 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[SEPTIN8]] | -0.56 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[FH]] | -0.56 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[HMGN1]] | -0.55 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[MBNL3]] | -0.54 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[MOB1A]] | -0.54 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[DR1]] | -0.54 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[EIF4G1]] | -0.54 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[TUG1]] | -0.54 | -0.36 / -0.49 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESRP2]] | B | ESRP2 activity raises TRMT112's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 1.38× lower at baseline in the lines without ESRP2 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-48.0, -26.8); signed map (-62.4, -2.4). **Vector** length 83.6, 34.9% of its response variance represented; |z| ≥ 3 in 511 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Peptide chain elongation* (reactome, mean cos +0.66 to 19); *PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA* (reactome, mean cos +0.66 to 19); *Viral mRNA Translation* (reactome, mean cos +0.66 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +3.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.9 | +1.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.8 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.3 | +1.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +0.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +1.6 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -5.8 | +4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.3 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -5.0 | +7.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.3 | +1.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.4 | -0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | +0.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.0 | -0.4 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -2.0 | -0.4 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | tRNA methyltransferase activator subunit 11-2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,316,460-64,317,559 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC152, HSPC170, TRM112, TRMT11-2, hTrm112 |
| Reactome | 11 pathways, smallest: Methylation; tRNA modification in the nucleus and cytosol; Phase II - Conjugation of compounds |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UI30](https://www.uniprot.org/uniprotkb/Q9UI30) (Multifunctional methyltransferase subunit TRM112-like protein):

> Acts as an activator of both rRNA/tRNA and protein methyltransferases. Together with methyltransferase BUD23, methylates the N(7) position of a guanine in 18S rRNA. The heterodimer with N6AMT1/HEMK2 catalyzes N5-methylation of ETF1 on 'Gln-185', using S-adenosyl L-methionine as methyl donor. The heterodimer with N6AMT1/HEMK2 also monomethylates 'Lys-12' of histone H4 (H4K12me1). The heterodimer with ALKBH8 catalyzes the methylation of 5-carboxymethyl uridine to 5-methylcarboxymethyl uridine at …

**Summary**, from NCBI Gene [51504](https://www.ncbi.nlm.nih.gov/gene/51504):

> Enables protein heterodimerization activity; protein methyltransferase activity; and tRNA methyltransferase activator activity. Involved in RNA metabolic process; peptidyl-glutamine methylation; and positive regulation of rRNA processing. Located in nucleoplasm and perinuclear region of cytoplasm. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26940](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26940) · Entrez [51504](https://www.ncbi.nlm.nih.gov/gene/51504) · UniProt [Q9UI30](https://www.uniprot.org/uniprotkb/Q9UI30) · Ensembl [ENSG00000173113](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173113)

## Data

Gene col 10340: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10340); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10340, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10340]; `tensor/DDL_lfc|DDL_z.npy` [10340]; `embed/gene_vectors.npy` [10340]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10340 or target_col == 10340). Every well: [[TRMT112 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRMT112.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
